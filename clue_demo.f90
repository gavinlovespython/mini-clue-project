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

  print *, "Fortran clue demo:"
  print *, "-------------------"

  do i = 1, size(clues)
     print *, " - ", trim(clues(i))
  end do

  print *, ""
  print *, "End of Fortran demo."
end program clue_demo
