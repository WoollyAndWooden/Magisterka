import org.apache.pekko.actor.{Actor, ActorSystem, Props, ActorRef, Terminated}
import scala.io.StdIn
import scala.util.Random
import scala.concurrent.Await
import scala.concurrent.duration.Duration

case object ShootingOrderHPtC
case object ShootingOrderCtD
case object ShootingEnemyCastle
case class GettingShotDefender(noDefenders: Int)
case class EnemySetCastle(enemy: ActorRef)
case class EnemySetDefenders(enemy: ActorRef)

class Castle extends Actor {
  var defenders: Seq[ActorRef] = (1 to 100).map {i => context.actorOf(Props(new Defender))}
  defenders.foreach {context.watch}
  var enemy: Option[ActorRef] = None

  override def receive: Receive = {
    case EnemySetCastle(ref) =>
        enemy = Some(ref)
        enemy match {
          case Some(enemy) => defenders.foreach(defender => defender ! EnemySetDefenders(ref))
          case None => println("...")
        }
      
    
    case Terminated(deadActorRef) =>
      defenders = defenders.filterNot(_ == deadActorRef)
      if(defenders.size == 0) then context.system.terminate()

    case ShootingOrderHPtC =>
      defenders.foreach(defender => defender ! ShootingOrderCtD)

    case ShootingEnemyCastle =>
      defenders(Random.nextInt(defenders.size)) ! GettingShotDefender(defenders.size)
  } 
}

class Defender extends Actor {
  var enemy: Option[ActorRef] = None
  override def receive: Receive = {
    case EnemySetDefenders(ref) =>
      enemy = Some(ref)

    case ShootingOrderCtD =>
      enemy match {
        case Some(enemy) => enemy ! ShootingEnemyCastle
        case None => println("NOT WORKING")
      }

    case GettingShotDefender(noDefenders) =>
      Random.nextInt(200) < noDefenders match {
        case true =>
          println("DIED")
          context.stop(self)
        case false => println("MISSED")
      }
  }
}

object HigherForce extends App {
  val system = ActorSystem("WarGame")
  var castle1: ActorRef = system.actorOf(Props(new Castle))
  var castle2: ActorRef = system.actorOf(Props(new Castle))
  castle1 ! EnemySetCastle(castle2)
  castle2 ! EnemySetCastle(castle1)

  while (!system.whenTerminated.isCompleted) {
    
    println("FIRE!")
    castle1 ! ShootingOrderHPtC
    castle2 ! ShootingOrderHPtC

    // Wait 1 second before next volley
    Thread.sleep(1000)
  }

}