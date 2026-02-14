import org.apache.pekko.actor.{Actor, ActorSystem, Props, ActorRef}
import scala.io.StdIn
import scala.util.Random
import scala.concurrent.Await
import scala.concurrent.duration.Duration

case class Ball(playerCount: Int)

case class SetNext(player: ActorRef)

class Player(name: String, roundCount: Int) extends Actor {

  var nextPlayer: Option[ActorRef] = None
  var roundsLeft: Int = roundCount

  override def receive: Receive = {
    case SetNext(ref) =>
      nextPlayer = Some(ref)
    case Ball(playerCount) =>
      println(s"$name: caught the ball, $roundsLeft catches left")
      Thread.sleep(200)
      nextPlayer match {
        case Some(nextPlayer) =>
          (playerCount, roundsLeft) match {
            case (1, _) => 
              println(s"$name LAST MAN STANDING")
              context.system.terminate()
            case (_, 0) =>
              println(s"$name LEAVES THE MATCH")
              sender() ! SetNext(nextPlayer)
              nextPlayer ! Ball(playerCount - 1)
              //context.stop(self)

            case (_, _) =>
              roundsLeft -= 1
              nextPlayer ! Ball(playerCount)
          }
        case None => println("HUH")
      }
  }
}

object PingPong extends App {
  val system = ActorSystem("PekkoPingPong")

  val numPlayers = Random.nextInt(10)+2
  println(numPlayers)
  (numPlayers > 2) match {
    case true => 
      val players: Seq[ActorRef] = (1 to numPlayers).map {i => system.actorOf(Props(new Player(s"Player $i", Random.nextInt(numPlayers)+10)), s"p$i")}
      players.zip(players.tail :+ players.head).foreach {case (current, next) => current ! SetNext(next)}
      println(s"Players are defined, kicking of the game!")

      players.head ! Ball(numPlayers)

      //Await.result(system.whenTerminated, Duration.Inf)
    case false =>
      println("Not enough players")
      system.terminate()
  }
}
