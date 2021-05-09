.. _label-opbend:

Out-of-Plane Bending
====================

Tinker has implemented two types of out-of-plane bending angles. In the Wilson-Decius-Cross formulation :cite:`Wilson1980`, the out-of-plane angle :math:`\chi` associated with bond *BD* in :numref:`fig-anglep` is the angle between *BD* and plane *ADC*, whereas the Allinger formulation uses the angle between *BD* and plane *ABC*. Similar to harmonic bond stretching, the following functional form has been implemented in Tinker:

.. math::

   U = k\chi^2(1 + k_3\chi + k_4\chi^2).
