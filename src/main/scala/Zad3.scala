@main
def zad73: Unit = {
 val linie = io.Source
  .fromResource("ogniem-i-mieczem.txt")
  .getLines.toList
  
 def histogram(maks: Int): String = {
  for {
    c <- linie.mkString.filter(_.isLetter).map(_.toLower).groupBy(identity).view.mapValues(_.size).toList
    maxCount <- c.map(_._2).maxOption.getOrElse(0)
    (char, count) <- c.sortBy(_._1)

    len <- (count.toDouble / maxCount * maks).toInt
  } yield s"$char: ${"*" * len}".mkString("\n")

 }

 println(histogram(20))
}
