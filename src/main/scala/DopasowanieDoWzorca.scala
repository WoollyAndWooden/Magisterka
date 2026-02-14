import scala.annotation.tailrec

@main def DopasowanieDoWzorca(): Unit = {

  // Zadanie 1. Napisz generyczną funkcję
  // def divide[A](list: List[A]): (List[A], List[A]) = /* ... */
  // która podzieli listę list na dwie części. W pierwszej będą się znajdywać elementy na parzystych indeksach w drugiej elementy na nieparzystych.
  def divide[A](list: List[A]): (List[A], List[A]) = {
    @tailrec
    def div(list: List[A], even: List[A], odd: List[A], i: Int): (List[A], List[A]) = {
      list match {
        case h :: t => (i % 2) match {
          case 0 => div(t, h :: even, odd, i + 1)
          case _ => div(t, even, h :: odd, i + 1)
        }
        case _ => (even.reverse, odd.reverse)
      }
    }
    div(list, List(), List(), 1)
  }

  // Zadanie 2. Zdefiniuj generyczną funkcję
  // def merge[A](a: List[A], b: List[A])(leq: (A, A) => Boolean): List[A]
  // która połączy ze sobą dowolne dwa ciągi elementów typu A, zgodnie z porządkiem zadanym przez funkcję leq (załóżmy, że ciągi są posortowane).
  def merge[A](a: List[A], b: List[A])(leq: (A, A) => Boolean): List[A] = {
    @tailrec
    def mergeRec(a: List[A], b: List[A], acc: List[A]): List[A] = {
      (a, b) match {
        case (ha :: ta, hb  :: tb) => leq(ha, hb) match {
          case true => mergeRec(ta, b, ha :: acc)
          case false => mergeRec(a, tb, hb :: acc)
        }
        case (Nil, hb :: tb) => mergeRec(a, tb, hb :: acc)
        case (ha :: ta, Nil) => mergeRec(ta, b, ha :: acc)
        case (Nil, Nil) => acc.reverse
      }
    }
    mergeRec(a, b, List())
  }

  // Zadanie 3. Napisz generyczną funkcję
  // def compress[A](list: List[A]): List[(A, Int)]
  // która w liście list zastępuje każdy podciąg powtarzających się elementów a...a parą (a, długość podciągu).
  def compress[A](list: List[A]): List[(A, Int)] = {
    @tailrec
    def compressHelper(list: List[A], e: A, eOcurr: Int, ret: List[(A, Int)]): List[(A, Int)] = {
      list match {
        case h :: t => if (h == e) then compressHelper(t, e, eOcurr + 1, ret) else compressHelper(t, h, 1, (e, eOcurr) :: ret)
        case Nil => (e, eOcurr) :: ret
      }
    }
    compressHelper(list.tail, list.head, 1, List()).reverse
  }

  // Zadanie 4. Zdefiniuj generyczną funkcję
  // def isSub[A](l: List[A], lSub: List[A]): Boolean = /* ... */
  // która zwróci informację czy wszystkie elementy w lSub znajdują się w l. Możesz założyć, że elementy w lSub są unikatowe.
  def isSub[A](l: List[A], lSub: List[A]): Boolean = {
    @tailrec
    def isSubHelper(l: List[A], lSub: List[A], orgL: List[A]): Boolean = {
      (l, lSub) match {
        case (h :: t, hsub :: tsub) => if (h == hsub) then isSubHelper(orgL, tsub, orgL) else isSubHelper(t, lSub, orgL)
        case (Nil, _) => false
        case (_, Nil) => true
      }
    }
    isSubHelper(l, lSub, l)
  }

  // Zadanie 5. Zdefiniuj generyczną funkcję
  // def compute[A, B](l: List[Option[A]])(op1: A => B)(op2: (A, B) => B): Option[B] = /* ... */
  // która korzystając z funkcji op1 (dla pierwszej wartości niepustej) i op2 (dla pozostałych niepustych wartości), obliczy "wartość" listy l.
  def compute[A, B](l: List[Option[A]])(op1: A => B)(op2: (A, B) => B): Option[B] = {
    @tailrec
    def computeHelper(l: List[Option[A]], ret: Option[B]): Option[B] = {
      (l, ret) match {
        case (Nil, _) => ret
        case (None :: t, _) => computeHelper(t, ret)
        case (Some(h) :: t, None) => computeHelper(t, Some(op1(h)))
        case (Some(h) :: t, Some(b)) => computeHelper(t, Some(op2(h, b)))
      }
    }
    computeHelper(l, None)
  }

  // Zadanie 6. Zapoznaj się z możliwością zwracania funkcji, przez funkcję.
  // Zdefiniuj następujące generyczne operujące na funkcjach:
  // składanie funkcji:
  def compose[A, B, C](f: A => B)(g: B => C): A => C = {
    (a: A) => g(f(a))
  }
  // iloczyn funkcji:
  def prod[A, B, C, D](f: A => C, g: B => D): (A, B) => (C, D) = {
    (a: A, b: B) => (f(a), g(b))
  }
  // podniesienie operatora op: (T, T) => T
  def lift[A, B, T](op: (T,T) => T)(f: A => T, g: B => T): (A,B) => T = {
    (a: A, b: B) => op(f(a), g(b))
  }
  
  // Niech MSet[A] oznacza multi-zbiór (zbiór w którym elementy mogą się powtarzać) typu A.
  type MSet[A] = A => Int
  
  // Korzystając z funkcji w podpunkcie a zdefiniuj funkcję wykonujące operację: sumy, różnicy oraz części wspólnej dla wielozbiorów:
  def sum[A](s1: MSet[A], s2: MSet[A]): MSet[A] = {
    throw new NotImplementedError("Zadanie 6d: Uzupełnij implementację funkcji sum")
  }
  def diff[A](s1: MSet[A], s2: MSet[A]): MSet[A] = {
    throw new NotImplementedError("Zadanie 6e: Uzupełnij implementację funkcji diff")
  }
  def mult[A](s1: MSet[A], s2: MSet[A]): MSet[A] = {
    throw new NotImplementedError("Zadanie 6f: Uzupełnij implementację funkcji mult")
  }

  println("--- Zadania: Dopasowanie do wzorca ---")

  try {
    println("\nZadanie 1: divide")
    println(s"divide(List(1, 3, 5, 6, 7)) == ${divide(List(1, 3, 5, 6, 7))}")
  } catch { case e: NotImplementedError => println(e.getMessage) }

  try {
    println("\nZadanie 2: merge")
    val a = List(1, 3, 5, 8)
    val b = List(2, 4, 6, 8, 10, 12)
    println(s"merge(List(1,3,5,8), List(2,4,6,8,10,12))(...) == ${merge(a, b)(_ < _)}")
  } catch { case e: NotImplementedError => println(e.getMessage) }

  try {
    println("\nZadanie 3: compress")
    val list_c = List('a','a','b','c','c','c','d','d','c')
    println(s"compress(...) == ${compress(list_c)}")
  } catch { case e: NotImplementedError => println(e.getMessage) }

  try {
    println("\nZadanie 4: isSub")
    val lSub = List('a', 'b', 'c')
    val l = List('b', 'o', 'c', 'i', 'a', 'n')
    println(s"isSub(...) == ${isSub(l, lSub)}")
  } catch { case e: NotImplementedError => println(e.getMessage) }

  try {
    println("\nZadanie 5: compute")
    val list_comp = List(Some(1), None, Some(2), None, Some(3), Some(4))
    println(s"compute(...) == ${compute(list_comp)(_ + 0)(_ + _)}")
  } catch { case e: NotImplementedError => println(e.getMessage) }

  try {
    println("\nZadanie 6: Funkcje wyższego rzędu i MSet")
    // Test dla `sum`
    val s1: MSet[Int] = (n: Int) => n match { case 1 => 2; case 3 => 1; case _ => 0 }
    val s2: MSet[Int] = (n: Int) => n match { case 1 => 1; case 2 => 3; case _ => 0 }
    val s_sum = sum(s1, s2)
    // Oczekiwane: s_sum(1) == 3, s_sum(2) == 3, s_sum(3) == 1
    println(s"sum(s1,s2)(1) == ${s_sum(1)}")
    println(s"sum(s1,s2)(2) == ${s_sum(2)}")
    println(s"sum(s1,s2)(3) == ${s_sum(3)}")
  } catch { case e: NotImplementedError => println(e.getMessage) }
}
