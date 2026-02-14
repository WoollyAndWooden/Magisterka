@main def MetodyKolekcji(): Unit = {

  // === Grupa 1 ===

  // Zadanie 1. Korzystając z metod drop i take, zdefiniuj funkcję:
  def subSeq[A](seq: Seq[A], begIdx: Int, endIdx: Int): Seq[A] = {
    seq.take(endIdx).drop(begIdx);
  }

  // Zadanie 2. Korzystając z metod filter, map i zipWithIndex, zdefiniuj funkcję:
  def remElem[A](seq: Seq[A], k: Int): Seq[A] = {
    seq.zipWithIndex.filter {case (_, i) => i != k}.map {case (e, _) => e}
  }

  // Zadanie 3. Korzystając z metody zip i innych metod, zdefiniuj funkcję:
  def diff[A](seq1: Seq[A], seq2: Seq[A]): Seq[A] = {
    seq1.zip(seq2). filter {case (a, b) => a != b}.map{case (a, _) => a}
  }

  // Zadanie 4. Korzystając z metody foldLeft/foldRight, zdefiniuj funkcję:
  def sumOption(seq: Seq[Option[Double]]): Double = {
    seq.foldLeft(0.0)((acc, x) => x match{
      case None => acc
      case Some(v) => acc+v})
  }

  // Zadanie 5. Korzystając z metody foldLeft/foldRight, zdefiniuj generyczną funkcję:
  def deStutter[A](seq: Seq[A]): Seq[A] = {
    seq.foldLeft(Seq.empty[A]) {(acc, x) => acc.lastOption match {
        case Some(last) => (last == x) match {
            case true => acc
            case false => acc :+ x
        }
        case _ => acc :+ x
    }}    
  }

  // Zadanie 6. Korzystając z metody sliding i innych metod, zdefiniuj funkcję:
  def isOrdered[A](seq: Seq[A])(leq:(A, A) => Boolean): Boolean = {
    seq.sliding(2).forall {
        case Seq(a, b) => leq(a, b)
        case _ => true
    }
  }

  // Zadanie 7. Korzystając z metody groupBy i innych metod, zdefiniuj funkcję:
  def freq[A](seq: Seq[A]): Set[(A, Int)] = {
    seq.groupBy(identity).view.mapValues(_.size).toMap.toSet
  }

  // Zadanie 8. Korzystając z metod sortBy, apply, zdefiniuj funkcję:
  def median(seq: Seq[(String, Double)]): Double = {
    (seq.sortBy(_._2).apply((seq.size - 1) / 2)._2 + seq.sortBy(_._2).apply(seq.size / 2)._2) / 2.0
  }

  // Zadanie 9. Korzystając z metod minBy, maxBy, zdefiniuj funkcję:
  def minMax(seq: Seq[(String, Double)]): Option[(String, String)] = {
    Some(seq.minBy(_._2)._1, seq.maxBy(_._2)._1)
  }

  // Zadanie 10. Korzystając z "wyliczenia" for/yield, zdefiniuj funkcję:
  def threeNumbers(n: Int): Set[(Int, Int, Int)] = {
    (for { 
      a <- 1 to n 
      b <- (a + 1) to n 
      c <- (b + 1) to n
      if(a * a + b * b == c * c)
      } yield (a, b, c)).toSet
  }
  
  // === Grupa 2 ===
  
  // Zadanie 1. Korzystając z metod oferowanych przez kolekcje zdefiniuj funkcję:
  def countChars(str: String): Int = {
    str.groupBy(identity).toSet.size
  }
  
  // Zadanie 2. Korzystając z metod oferowanych przez kolekcje zdefiniuj funkcję:
  def minNotCon(set: Set[Int]): Int = {
    (0 to set.size).find(i => !set.contains(i)).getOrElse(set.max + 1)
  }

  // Zadanie 3. Korzystając z metod oferowanych przez kolekcje zdefiniuj funkcję:
  def swap[A](seq: Seq[A]): Seq[A] = {
    throw new NotImplementedError("Zadanie 2.3: Uzupełnij implementację funkcji swap")
  }
  
  // Zadanie 4. Wyszukaj strefy w Europie i posortuj.
  def europeanTimeZones(): Seq[String] = {
    val strefy: Seq[String] = java.util.TimeZone.getAvailableIDs.toSeq
    throw new NotImplementedError("Zadanie 2.4: Uzupełnij implementację sortowania stref")
  }

  // Zadanie 5. Korzystając z funkcji kolekcji zdefiniuj funkcję:
  def score(code: Seq[Int])(move: Seq[Int]): (Int, Int) = {
    throw new NotImplementedError("Zadanie 2.5: Uzupełnij implementację funkcji score")
  }

  // Zadanie 6. Obliczanie wyników zawodów sportowych
  type PartialResult = (String, String, Int, Int)
  type FinalResult = (Int, String, String, (Double, Double))
  def calculateRanking(results: List[PartialResult]): List[FinalResult] = {
    throw new NotImplementedError("Zadanie 2.6: Uzupełnij implementację funkcji calculateRanking")
  }


  println("--- Zadania: Metody kolekcji ---")
  
  try {
    println("\nZadanie 1.1: subSeq")
    println(s"subSeq(Seq(1,2,3,4,5), 1, 3) == ${subSeq(Seq(1,2,3,4,5), 1, 3)}")
  } catch { case e: NotImplementedError => println(e.getMessage) }
  
  try {
    println("\nZadanie 1.2: remElem")
    println(s"remElem(Seq(1,2,3,4,5), 2) == ${remElem(Seq(1,2,3,4,5), 2)}")
  } catch { case e: NotImplementedError => println(e.getMessage) }
  
  try {
    println("\nZadanie 1.3: diff")
    println(s"diff(Seq(1, 2, 3), Seq(2, 2, 1, 3)) == ${diff(Seq(1, 2, 3), Seq(2, 2, 1, 3))}")
  } catch { case e: NotImplementedError => println(e.getMessage) }
  
  try {
    println("\nZadanie 1.4: sumOption")
    val seq_sum = Seq(Some(5.4), Some(-2.0), Some(1.0), None, Some(2.6))
    println(s"sumOption(...) == ${sumOption(seq_sum)}")
  } catch { case e: NotImplementedError => println(e.getMessage) }
  
  try {
    println("\nZadanie 1.5: deStutter")
    println(s"deStutter(Seq(1,1,2,4,4,4,1,3)) == ${deStutter(Seq(1, 1, 2, 4, 4, 4, 1, 3))}")
  } catch { case e: NotImplementedError => println(e.getMessage) }
  
  try {
    println("\nZadanie 1.6: isOrdered")
    println(s"isOrdered(Seq(1,2,2,4))(_ < _) == ${isOrdered(Seq(1, 2, 2, 4))(_ < _)}")
    println(s"isOrdered(Seq(1,2,2,4))(_ <= _) == ${isOrdered(Seq(1, 2, 2, 4))(_ <= _)}")
  } catch { case e: NotImplementedError => println(e.getMessage) }
  
  try {
    println("\nZadanie 1.7: freq")
    println(s"freq(Seq('a','b','a','c','c','a')) == ${freq(Seq('a','b','a','c','c','a'))}")
  } catch { case e: NotImplementedError => println(e.getMessage) }

  try {
    println("\nZadanie 1.8: median")
    val scores = Seq(("A", 10.0), ("B", 20.0), ("C", 15.0))
    println(s"median(...) == ${median(scores)}")
  } catch { case e: NotImplementedError => println(e.getMessage) }
  
  try {
    println("\nZadanie 1.9: minMax")
    val scores = Seq(("A", 10.0), ("B", 20.0), ("C", 5.0))
    println(s"minMax(...) == ${minMax(scores)}")
  } catch { case e: NotImplementedError => println(e.getMessage) }
  
  try {
    println("\nZadanie 1.10: threeNumbers")
    println(s"threeNumbers(20) == ${threeNumbers(20)}")
  } catch { case e: NotImplementedError => println(e.getMessage) }
  
  try {
    println("\nZadanie 2.1: countChars")
    println(s"countChars(\"abracadabra\") == ${countChars("abracadabra")}")
  } catch { case e: NotImplementedError => println(e.getMessage) }
  
  try {
    println("\nZadanie 2.2: minNotCon")
    println(s"minNotCon(Set(-3, 0, 1, 2, 5, 6)) == ${minNotCon(Set(-3, 0, 1, 2, 5, 6))}")
  } catch { case e: NotImplementedError => println(e.getMessage) }
  
  try {
    println("\nZadanie 2.3: swap")
    println(s"swap(Seq(1, 2, 3, 4, 5)) == ${swap(Seq(1, 2, 3, 4, 5))}")
  } catch { case e: NotImplementedError => println(e.getMessage) }
  
  try {
    println("\nZadanie 2.4: europeanTimeZones")
    println(s"europeanTimeZones().take(5) == ${europeanTimeZones().take(5)}")
  } catch { case e: NotImplementedError => println(e.getMessage) }
  
  try {
    println("\nZadanie 2.5: score (MasterMind)")
    val code = Seq(1, 3, 2, 2, 4, 5)
    val move = Seq(2, 1, 2, 4, 7, 2)
    println(s"score(...) == ${score(code)(move)}")
  } catch { case e: NotImplementedError => println(e.getMessage) }

  try {
    println("\nZadanie 2.6: calculateRanking")
    val partials = List(
      ("Jan", "Kowalski", 10, 15),
      ("Anna", "Nowak", 12, 12),
      ("Jan", "Kowalski", 14, 11)
    )
    println(s"calculateRanking(...) == ${calculateRanking(partials)}")
  } catch { case e: NotImplementedError => println(e.getMessage) }

}
