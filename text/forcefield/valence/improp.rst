.. _label-improp:

Improper Dihedral
=================

Commonly used in the CHARMM force fields, this potential function is meant to keep atoms planar. The ideal angle :math:`\phi_0` defined by dihedral *D-A-B-C* will always be zero degrees. *D* is the trigonal atom, *A-B-C* are the peripheral atoms. In the original CHARMM parameter files, the trigonal atom is often listed last as *C-B-A-D*.

Some of the improper angles are "double counted" in the CHARMM protein parameter set. Since Tinker uses only one improper parameter per site, we have doubled these force constants in the Tinker version of the CHARMM parameters. Symmetric parameters, which are the origin of the "double counted" CHARMM values, are handled in the Tinker package by assigning all symmetric states and using the Tinker force constant divided by the symmetry number.

The harmonic functional form implemented in Tinker is

.. math::

   U = k(\phi-\phi_0)^2.

There is no coefficient 1/2 before the force coefficient, which may be different in other software packages.
