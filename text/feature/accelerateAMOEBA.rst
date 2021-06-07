Accelerating MD Simulation in Tinker9
=====================================

.. include:: ../replace.rst

|to9|

Cutoff distances.
   In most cases, the AMOEBA force field will use both VDW and electrostatic potential energies. The latter term usually contains both permanent quadrupole and induced dipole energies and enables PME. The performance of Tinker9 is very sensitive to the cutoff distances of these nonbonded terms and is especially dominated by the cutoff distance of the electrostatics.

   Depending on the nature of the systems of interest, the VDW cutoff is usually set between 9 to 12 |ang|. The isotropic long-range VDW correction can optionally be enabled with negligible overhead. The typical cutoff distance is 7 |ang| for multipole and induced dipole PME and 9 |ang| for partial charge PME./

   For a partial charge force field, the performance of Tinker9 is no longer dominated by electrostatics. VDW and partial charge PME become comparable, or VDW may even become dominant if the VDW cutoff is significantly longer than the PME cutoff due to the cubic-to-quartic growth of the number of interactions. Therefore, it is a common practice for some partial charge force fields to set two cutoffs to the same distance, e.g., 9 |ang|. Tinker9 will launch an optimized CUDA kernel that combines the Lennard-Jones and partial charge potentials if it detects that two cutoffs are equal.

   .. seealso::

      EWALD, EWALD-CUTOFF, VDW-CUTOFF, VDW-CORRECTION

Neighbor list and list buffer.
   Using neighbor lists, Tinker9 will prioritize the use of CUDA kernels with optimized spatial decomposition algorithms, instead of the classic Verlet Lists. The trade-off of using a longer list buffer is that the reconstruction or update of the neighbor is less frequent but the possible number of pairwise interactions is greater. Since the default value of the list buffer in Tinker9 is inherited from the canonical Tinker, it may not be optimized for Tinker9's spatial decomposition algorithms. The optimized length of the list buffer varies with different systems and can be approximately determined by benchmarking a few short simulations.

   .. seealso::

      NEIGHBOR-LIST, LIST-BUFFER

PME order.
   The order of the B-spline interpolation for partial charge PME can be set to 4 to improve the performance. This value should not be changed for multipole or induced dipole PME.

   .. seealso::

      PME-ORDER

Induced dipoles.
   The default convergence criterion for the self-consistent induced dipoles is very tight. In general, users can safely relax it to :math:`10^{-5}`. Using a prediction algorithm can further reduce the number of iterations. For Tinker9, the Always Stable Predictor-Corrector (ASPC) method is recommended. The standard Gear extrapolation method (GEAR) and extrapolation based on a least squared prediction (LSQR) method are available in Tinker9 as well. ASPC is an advanced version of GEAR. LSQR may endure numerical instability due to the limited floating-point precision.

   If a very loose convergence criterion is set, e.g., 0.01, no prediction method should be used. Otherwise, the errors in the induced dipoles will be extremely biased towards the induced dipoles obtained in the previous MD steps.

   .. seealso::

      POLAR-EPS, POLAR-PREDICT

Keywords example:

.. code-block:: text

   ewald
   ewald-cutoff      7.0
   vdw-cutoff       10.0
   vdw-correction
   neighbor-list
   list-buffer       0.7
   pme-order           5
   polar-eps      1.0e-5
   polar-predict    aspc
