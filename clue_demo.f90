! ============================================
! Fortran Clue Demo
! A tiny standalone module for the polyglot set
! ============================================

program clue_demo
  implicit none

  character(len=*), parameter :: clues(3) = [ &
       "fortran still lives", &
       "clues can be classic", &
       "arrays start at one" ]

  integer :: i

  print *, "========================="
  print *, "   Fortran Clue Demo"
  print *, "========================="
  print *, "Total clues:", size(clues)
  print *, ""

  do i = 1, size(clues)
     print *, " - ", trim(clues(i))
  end do

  print *, ""
  print *, "End of Fortran demo."
end program clue_demo
