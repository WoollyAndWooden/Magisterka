@main
def zad72: Unit = {
 val linie = io.Source
  .fromResource("nazwiska.txt")
  .getLines.toList

  val result = for {
    x <- linie
    if (x.distinct.length, x.length) == linie.map(w => (w.distinct.length, w.length)).max
  } yield x

  println(result)
 }
