import scala.annotation.tailrec

@main def RekurencjaOgonowa(): Unit = {

  // Zadanie 1. Zdefiniuj funkcję reverse(str: String): String, która zwróci odwrócony napis pobrany jako argument.
  // Rozwiąż to zadanie bez korzystania ze zmiennych oraz wykorzystaj rekurencję ogonową.
  def reverse(str: String): String = {
    @tailrec
    def revTail(str: String, acc: String, len: Int): String = {
      str match {
        case "" => acc
        case _ => revTail(str.dropRight(1), acc + str(len), len - 1)
      }
    }
    revTail(str, "", str.length() - 1)
  }
  

  // Zadanie 2. Zdefiniuj funkcję isPrime(n: Int): Boolean która sprawdza, czy argument jest liczba pierwszą.
  // Rozwiąż to zadanie bez korzystania ze zmiennych oraz wykorzystaj rekurencję ogonową.
  def isPrime(n: Int): Boolean = {
    @tailrec
    def primeRev(n: Int, div: Int): Boolean = {
      div match {
        case 1 => true
        case _ => if (n % div != 0) then primeRev(n, div - 1) else false
      }
    }
    primeRev(n, n/2)
  }

  // Zadanie 3. Zdefiniuj funkcję binToDec(bin: Int): Int, która jako argument otrzyma liczbę zapisaną w systemie binarnym i przeliczy ją na system dziesiętny.
  // Rozwiąż to zadanie bez korzystania ze zmiennych oraz wykorzystaj rekurencję ogonową.
  def binToDec(bin: Int): Int = {
    @tailrec
    def binRev(bin: Int, i: Int, acc: Int): Int = {
      bin match {
        case 0 => acc
        case _ => binRev(bin / 10, i * 2, acc + (bin % 10) * i)
      }
    }
    binRev(bin, 1, 0)
  }

  // Zadanie 4. Zdefiniuj funkcję value(n: Int): Int, która zwróci n-ty wyrażony wzorem:
  // F(0) = 2
  // F(1) = 1
  // F(n) = F(n-1) + F(n-2) dla n > 1
  // Rozwiąż to zadanie bez korzystania ze zmiennych oraz wykorzystaj rekurencję ogonową.
  // Pierwsze 10 wyrazów ciągu: 2, 1, 3, 4, 7, 11, 18, 29, 47, 76.
  def value(n: Int): Int = {
    @tailrec
    def valRec(n: Int, a: Int, b: Int): Int = {
      n match {
        case 1 => a
        case _ => valRec(n-1, b, a + b)
      }
    }
    valRec(n, 2, 1)
  }

  // Zadanie 5. Używając rekurencji ogonowej, zdefiniuj funkcję
  // def isOrdered(tab: Array[Int], mlr: (Int, Int) => Boolean): Boolean
  // która sprawdza, czy tablica liczb całkowitych będąca jej argumentem jest uporządkowana zgodnie z porządkiem definiowanym przez funkcję mlr.
  // Rozwiąż to zadanie bez korzystania ze zmiennych.
  def isOrdered(tab: Array[Int], mlr: (Int, Int) => Boolean): Boolean = {
    /*@tailrec
    def checkRec(tab:Array[Int], mlr: (Int, Int) => Boolean): Boolean = {
      true
    }*/
    //checkRec(tab, mlr)
    true
  }

  // Zadanie 6. Zdefiniuj funkcję rekurencyjną ogonowo:
  // def worth(tab1: Array[Int], tab2: Array[Int])(pred: (Int, Int) => Boolean)(op: (Int, Int) => Int): Option[Int]
  // która zwróci wartość zwracaną przez op, dla pierwszych wartości, które znajdują się na tych samych pozycjach tablic oraz spełniają predykat pred. Jeżeli takie wartości nie istnieją, powinna zostać zwrócona wartość None.
  // Rozwiąż to zadanie bez korzystania ze zmiennych.
  def worth(tab1: Array[Int], tab2: Array[Int])(pred: (Int, Int) => Boolean)(op: (Int, Int) => Int): Option[Int] = {
    throw new NotImplementedError("Zadanie 6: Uzupełnij implementację funkcji worth")
  }

  println("--- Zadania: Rekurencja ogonowa ---")

  try {
    println("\nZadanie 1: reverse")
    println(s"reverse(\"student\") == ${reverse("student")}")
    println(s"reverse(\"kajak\") == ${reverse("kajak")}")
  } catch { case e: NotImplementedError => println(e.getMessage) }

  try {
    println("\nZadanie 2: isPrime")
    println(s"isPrime(7) == ${isPrime(7)}")
    println(s"isPrime(10) == ${isPrime(10)}")
  } catch { case e: NotImplementedError => println(e.getMessage) }
  
  try {
    println("\nZadanie 3: binToDec")
    println(s"binToDec(1010) == ${binToDec(1010)}")
    println(s"binToDec(111) == ${binToDec(111)}")
  } catch { case e: NotImplementedError => println(e.getMessage) }

  try {
    println("\nZadanie 4: value")
    println(s"value(5) == ${value(5)}")
    println(s"value(9) == ${value(9)}")
  } catch { case e: NotImplementedError => println(e.getMessage) }

  try {
    println("\nZadanie 5: isOrdered")
    val orderedTab1 = Array(1, 3, 3, 6, 8)
    println(s"isOrdered(Array(1, 3, 3, 6, 8), (_ <= _)) == ${isOrdered(orderedTab1, _ <= _)}")
    println(s"isOrdered(Array(1, 3, 3, 6, 8), (_ < _)) == ${isOrdered(orderedTab1, _ < _)}")
  } catch { case e: NotImplementedError => println(e.getMessage) }

  try {
    println("\nZadanie 6: worth")
    val worthTab1 = Array(-1, 3, 2, -8, 5)
    val worthTab2 = Array(-3, 3, 3, 0, -4, 5)
    println(s"worth(...) == ${worth(worthTab1, worthTab2)(_ < _)(_ + _)}")
  } catch { case e: NotImplementedError => println(e.getMessage) }

}
