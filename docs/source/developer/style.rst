FATES Style Guide
-----------

Code development has style considerations.  Should you capitalize variables.. or not?  How many characters should the maximum width of a text line be?  Should you use long blocks of ``====``   or ``-----`` to indicate visual breaks in code.   Do we like underscores or dashes?  

FATES Style Guide
^^^^^^^^^^^^^^^^^
.. highlight:: fortran
   
.. note::
   Note that style is evolving and existing code may not reflect what is in this document)

ALL fortran code should be bound in modules.  If for some reason this does not seem possible, please contact admin team.  Therefore, all fortran files should end in "Mod.F90".

Files should be named using "CamelCase".  CamelCase uses no underscores, capital letters are inserted to indicate the beginning of different words.

Subroutines and Functions should also use CamelCase.

Variables, and data structures should **not** use CamelCase, and should make use of underscores if need be.

Keep line lengths within 100 characters, consistently, when possible.  If it makes the code too hard to interpret exceptions are allowed.  Line lengths should never exceed 110 characters and will give NAG fits at 132.


Delineate subroutines by breaking them with (out to 100 characters)::
   
   !======================================================


Blocks of commented code, or concept breaks can be delineated with (out to 100 characters)::
   
   !------------------------------------------------------


If a loop or "if" structure spans more than 50 lines, add a comment that trails in-line with the closing "end if" or "end do", that re-iterates the opening statement. This helps immensely with code readability.  Alternatively, you can use explicit loop naming to ensure loop closure correctness.  Example::

   if(example_logical) then
   
   ! Assume there is a copious amount of code that happens between
   ! the opening and closing statement
   
   end if  ! if(example_logical) then
   
Example::

   outer_logical_loop: if(example_logical) then
   
   ! Assume there is a copious amount of code that happens between
   ! the opening and closing statement
   
   end if outer_logical_loop


No hard-coded values.  

Bad:  ``area_m2 = area_ha*10000``

Good: ``area_m2 = area_ha*ha_to_m2``

0 Constants should be given a defined type, label and "parameter" designation. Example::
   
   real(r8),parameter :: ha_to_m2 = 10000.0_r8 # This is the area conversion factor of hectares to square meters

Variables should have descriptive names.

Bad: ``b = c/a``

Good: ``leaf_nitrogen_mass = leaf_carbon_mass / leaf_cn_ratio``



