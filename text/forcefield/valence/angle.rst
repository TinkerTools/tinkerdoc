.. _label-angle:

Angle Bending
=============

Similar to bond stretching, angle bending term is also an empirical function of angle deviating from the ideal angle value, i.e., :math:`\Delta\theta=\theta-\theta_0`. Terms from cubic to sextic are added to generalize the *HARMONIC* functional form.

.. math::

   U = k\Delta\theta^2(1+k_3\Delta\theta+k_4\Delta\theta^2+k_5\Delta\theta^3+k_6\Delta\theta^4).

MMFF force field has a special treatment for *LINEAR* angle, e.g., carbon dioxide. Since the ideal angle should always be :math:`\pi` rad, the deviation can be approximated by

.. math::

   \Delta\theta =\theta-\pi =2(\frac{\theta}{2}-\frac{\pi}{2}) \sim 2\sin(\frac{\theta}{2}-\frac{\pi}{2}) =-2\cos\frac{\theta}{2}.

Only keeping the quadratic term, the angle bending term can be simplified to

.. math::

   U = 2k(1+\cos\theta).

The *LINEAR* angle type is a special case of the SHAPES-style Fourier potential function :cite:`Allured1991` with 1-fold periodicity, which is referred to as the *FOURIER* angle type in Tinker jargon and has the following form

.. math::

   U = 2k(1+\cos(n\theta-\theta_0)).

In addition, there is another *IN-PLANE* angle type for trigonal center atoms. One can project atom *D* to point *X* on plane *ABC*. Instead of angle *A-D-B*, the ideal and actual angle values are for angle *A-X-B* (see :numref:`fig-anglep`).

.. _fig-anglep:
.. figure:: ../../figure/anglep.*
   :width: 300 px
   :align: center

   A trigonal center and an in-plane angle.
