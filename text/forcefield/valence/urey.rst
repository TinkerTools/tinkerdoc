.. _label-urey:

Urey-Bradley Potential
======================

Urey-Bradley potential energy accounts for the 1-3 nonbonded interactions. The cubic and quartic terms are added to the harmonic functional form in Tinker:

.. math::

   U = k\Delta u^2(1 + k_3\Delta u + k_4\Delta u^2),

where :math:`\Delta u` is the difference of 1-3 distance deviating from its ideal value. Coefficients *k3* and *k4* are usually zero.
