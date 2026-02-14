@main
def zad71: Unit = {
 val linie = io.Source
  .fromResource("liczby.txt")
  .getLines.toList

  val result = for {
    x <- linie
    if x == x.sorted
    if x.map(_.asDigit).sum % 2 == 0
  } yield x
  println(result)

}
