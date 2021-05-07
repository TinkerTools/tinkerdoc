.. _label-bond:

Bond Stretching
===============

Bond term is an empirical function of bond deviating from the ideal bond length, i.e., :math:`\Delta b = b - b_0`. To support the AMOEBA force field, Tinker includes the 3rd and 4th order terms.

.. math::

    U = k\Delta b^2(1 + k_3\Delta b + k_4\Delta b^2).

.. note::

    Different from Hooke's Law, :math:`U=kx^2/2`, Tinker drops the coeffient 1/2.

The Morse oscillator is also implemented in Tinker:

.. math::

    U = D_e[1 - \exp(-a\Delta b)]^2.

Parameter *a* is hardwired to 2 by approximation. Following equation :math:`a = \sqrt{\frac{k}{2 D_e}}` and the Tinker convention to include 1/2 in the force constant, *De* is *k*/4.
