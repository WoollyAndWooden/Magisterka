import org.apache.pekko.actor.typed.*
import org.apache.pekko.actor.typed.scaladsl.*

trait MsgWordCounter
case class Init(liczbaPracownikow: Int) extends MsgWordCounter
case class Zlecenie(tekst: List[String]) extends MsgWordCounter
case class Wynik(liczbaSlow: Int, pracownik: ActorRef[MsgWorker]) extends MsgWordCounter

trait MsgWorker
case class Wykonaj(napis: String, replyTo: ActorRef[MsgWordCounter]) extends MsgWorker

object Pracownik {
  def apply(): Behavior[MsgWorker] = Behaviors.receive { (ctx, msg) =>
    msg match {
      case Wykonaj(napis, replyTo) =>
        val uniqueWordsCount = napis
          .split("\\s+")
          .filter(_.nonEmpty)
          .map(_.toLowerCase)
          .distinct
          .length
        
        replyTo ! Wynik(uniqueWordsCount, ctx.self)
        Behaviors.same
      case unknown =>
        ctx.log.error(s"Worker received unknown message: $unknown")
        Behaviors.unhandled
    }
  }
}

object Nadzorca {
  def apply(): Behavior[MsgWordCounter] = Behaviors.receive { (ctx, msg) =>
    msg match {
      case Init(n) =>
        ctx.log.info(s"Initializing with $n workers")
        val workers = (1 to n).map { i =>
          ctx.spawn(Pracownik(), s"worker-$i")
        }.toList
        ready(workers)
      case other =>
        ctx.log.error(s"Nadzorca not initialized! Received: $other")
        Behaviors.same
    }
  }

  private def ready(workers: List[ActorRef[MsgWorker]]): Behavior[MsgWordCounter] =
    Behaviors.receive { (ctx, msg) =>
      msg match {
        case Zlecenie(tekst) =>
          ctx.log.info("Received job. Distributing initial lines...")
          
          val (toProcess, remaining) = tekst.splitAt(workers.size)
          
          val activeWorkers = toProcess.zip(workers).map { case (line, worker) =>
            worker ! Wykonaj(line, ctx.self)
            worker
          }.toSet

          working(remaining, workers, activeWorkers.size, 0)
          
        case other =>
          ctx.log.error(s"Expected Zlecenie, received: $other")
          Behaviors.same
      }
    }

  private def working(
    remainingText: List[String],
    allWorkers: List[ActorRef[MsgWorker]],
    pendingResponses: Int,
    totalUniqueWords: Int
  ): Behavior[MsgWordCounter] = Behaviors.receive { (ctx, msg) =>
    msg match {
      case Wynik(count, worker) =>
        val newTotal = totalUniqueWords + count
        val stillPending = pendingResponses - 1

        remainingText match {
          case nextLine :: tail =>
            worker ! Wykonaj(nextLine, ctx.self)
            working(tail, allWorkers, pendingResponses, newTotal)
            
          case Nil if stillPending > 0 =>

            working(Nil, allWorkers, stillPending, newTotal)
            
          case Nil =>

            println(s"\n>>> FINAL RESULT: $newTotal unique words per line <<<\n")
            ready(allWorkers)
        }
      case other =>
        ctx.log.error(s"Unexpected message during processing: $other")
        Behaviors.same
    }
  }
}

@main
def zad1: Unit = {

  def dane(): List[String] = {
   scala.io.Source.fromResource("ogniem_i_mieczem.txt").getLines.toList
  }
  
  val system: ActorSystem[MsgWordCounter] = ActorSystem(Nadzorca(), "word-counter-system")

  system ! Init(liczbaPracownikow = 5)
  system ! Zlecenie(dane())
}
