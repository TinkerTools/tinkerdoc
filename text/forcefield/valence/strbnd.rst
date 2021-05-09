.. _label-strbnd:

Stretch-Bend Coupling
=====================

The functional forms for bond stretching, angle bending, and stretch-bend coupling are those of the MM3 force field :cite:`Allinger1989`:

.. math::

   U = (k_1\Delta b_1 + k_2\Delta b_2)\Delta\theta.

Even though force constants *k1* and *k2* are implemented as two independent variables in Tinker, they were treated as the same variable in the original
literature.
