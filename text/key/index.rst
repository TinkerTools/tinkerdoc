Use of the Keyword Control File
===============================

Using Keywords to Control Tinker Calculations
---------------------------------------------

This section contains detailed descriptions of the keyword parameters used to define or alter the course of a Tinker calculation. The keyword control file is optional in the sense that all of the Tinker programs will run in the absence of a keyfile and will simply use default values or query the user for needed information. However, the keywords allow use of a wide variety of algorithmic and procedural options, many of which are unavailable interactively.

Keywords are read from the keyword control file. All programs look first for a keyfile with the same base name as the input molecular system and ending in the extension .key. If this file does not exist, then Tinker tries to use a generic keyfile with the name Tinker.key and located in the same directory as the input system. If neither a system-specific nor a generic keyfile is present, Tinker will continue by using default values for keyword options and asking interactive questions as necessary.

Tinker searches the keyfile during the course of a calculation for relevant keywords that may be present. All keywords must appear as the first word on the line. Any blank space to the left of the keyword is ignored, and all contents of the keyfiles are case insensitive. Some keywords take modifiers; i.e., Tinker looks further on the same line for additional information, such as the value of some parameter related to the keyword. Modifier information is read in free format, but must be completely contained on the same line as the original keyword. Any lines contained in the keyfile which do not qualify as valid keyword lines are treated as comments and are simply ignored.

Several keywords take a list of integer values (atom numbers, for example) as modifiers. For these keywords the integers can simply be listed explicitly and separated by spaces, commas or tabs. If a range of numbers is desired, it can be specified by listing the negative of the first number of the range, followed by a separator and the last number of the range. For example, the keyword line ACTIVE 4 -9 17 23 could be used to add atoms 4, 9 through 17, and 23 to the set of active atoms during a Tinker calculation.

Keywords Grouped by Functionality
---------------------------------

Listed below are the available Tinker keywords sorted into groups by general function. The section ends with an alphabetical list containing each individual keyword, along with a brief description of its action, possible keyword modifiers, and usage examples.

OUTPUT CONTROL KEYWORDS
^^^^^^^^^^^^^^^^^^^^^^^

ARCHIVE	DEBUG	DIGITS
ECHO	EXIT-PAUSE	NOVERSION
OVERWRITE	PRINTOUT	SAVE-CYCLE
SAVE-FORCE	SAVE-INDUCED	SAVE-VELOCITY
VERBOSE	WRITEOUT

FORCE FIELD SELECTION KEYWORDS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

FORCEFIELD	PARAMETERS

POTENTIAL FUNCTION SELECTION KEYWORDS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

ANGANGTERM	ANGLETERM	BONDTERM
CHARGETERM	CHGDPLTERM	DIPOLETERM
EXTRATERM	IMPROPTERM	IMPTORSTERM
METALTERM	MPOLETERM	OPBENDTERM
OPDISTTERM	PITORSTERM	POLARIZETERM
RESTRAINTERM	RXNFIELDTERM	SOLVATETERM
STRBNDTERM	STRTORTERM	TORSIONTERM
TORTORTERM	UREYTERM	VDWTERM

POTENTIAL FUNCTION PARAMETER KEYWORDS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

ANGANG	ANGLE	ANGLE3
ANGLE4	ANGLE5	ANGLEF
ATOM	BIOTYPE	BOND
BOND3	BOND4	BOND5
CHARGE	DIPOLE	DIPOLE3
DIPOLE4	DIPOLE5	ELECTNEG
HBOND	IMPROPER	IMPTORS
METAL	MULTIPOLE	OPBEND
OPDIST	PIATOM	PIBOND
PITORS	POLARIZE	SOLVATE
STRBND	STRTORS	TORSION
TORSION4	TORSION5	TORTOR
UREYBRAD	VDW	VDW14
VDWPR

ENERGY UNIT CONVERSION KEYWORDS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

ANGLEUNIT	ANGANGUNIT	BONDUNIT
ELECTRIC	IMPROPUNIT	IMPTORUNIT
OPBENDUNIT	OPDISTUNIT	PITORSUNIT
STRBNDUNIT	STRTORUNIT	TORSIONUNIT
TORTORUNIT	UREYUNIT

LOCAL GEOMETRY FUNCTIONAL FORM KEYWORDS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

ANGLE-CUBIC	ANGLE-QUARTIC	ANGLE-PENTIC
ANGLE-SEXTIC	BOND-CUBIC	BOND-QUARTIC
BONDTYPE	MM2-STRBND	PISYSTEM
UREY-CUBIC	UREY-QUARTIC

VDW & REPULSION-DISPERSION FUNCTIONAL FORM KEYWORDS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A-EXPTERM	B-EXPTERM	C-EXPTERM
DELTA-HALGREN	DISP-12-SCALE	DISP-13-SCALE
DISP-14-SCALE	DISP-15-SCALE	EPSILONRULE
GAMMA-HALGREN	GAUSSTYPE	RADIUSRULE
RADIUSSIZE	RADIUSTYPE	VDW-12-SCALE
VDW-13-SCALE	VDW-14-SCALE	VDW-15-SCALE
VDW-CORRECTION	VDWINDEX	VDWTYPE

ELECTROSTATICS FUNCTIONAL FORM KEYWORDS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

CHG-12-SCALE	CHG-13-SCALE	CHG-14-SCALE
CHG-15-SCALE	CHG-BUFFER	DIELECTRIC
DIRECT-11-SCALE	DIRECT-12-SCALE	DIRECT-13-SCALE
DIRECT-14-SCALE	MPOLE-12-SCALE	MPOLE-13-SCALE
MPOLE-14-SCALE	MPOLE-15-SCALE	MUTUAL-11-SCALE
MUTUAL-12-SCALE	MUTUAL-13-SCALE	MUTUAL-14-SCALE
POLAR-12-SCALE	POLAR-13-SCALE	POLAR-14-SCALE
POLAR-15-SCALE	POLAR-ASPC	POLAR-EPS
POLAR-SOR	POLARIZATION	REACTIONFIELD

NONBONDED CUTOFF KEYWORDS
^^^^^^^^^^^^^^^^^^^^^^^^^

CHG-CUTOFF	CHG-TAPER	CUTOFF
DPL-CUTOFF	DPL-TAPER	HESS-CUTOFF
LIGHTS	MPOLE-CUTOFF	MPOLE-TAPER
NEIGHBOR-GROUPS	NEUTRAL-GROUPS	POLYMER-CUTOFF
TAPER	TRUNCATE	VDW-CUTOFF
VDW-TAPER

EWALD SUMMATION KEYWORDS
^^^^^^^^^^^^^^^^^^^^^^^^

DPME-GRID	DPME-ORDER	EWALD
EWALD-ALPHA	EWALD-BOUNDARY	EWALD-CUTOFF
PME-GRID	PME-ORDER	PPME-ORDER

CRYSTAL LATTICE & PERIODIC BOUNDARY KEYWORDS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A-AXIS	B-AXIS	C-AXIS
ALPHA	BETA	DODECAHEDRON
GAMMA	NO-SYMMETRY	OCTAHEDRON
SPACEGROUP	X-AXIS	Y-AXIS
Z-AXIS

NEIGHBOR LIST KEYWORDS
^^^^^^^^^^^^^^^^^^^^^^

CHG-LIST	LIST-BUFFER	MPOLE-LIST
NEIGHBOR-LIST	VDW-LIST

OPTIMIZATION KEYWORDS
^^^^^^^^^^^^^^^^^^^^^

ANGMAX	CAPPA	FCTMIN
HGUESS	INTMAX	LBFGS-VECTORS
MAXITER	NEWHESS	NEXTITER
SLOPEMAX	STEEPEST-DESCENT	STEPMAX
STEPMIN

MOLECULAR DYNAMICS KEYWORDS
^^^^^^^^^^^^^^^^^^^^^^^^^^^

BEEMAN-MIXING	DEGREES-FREEDOM	INTEGRATOR
REMOVE-INERTIA

THERMOSTAT & BAROSTAT KEYWORDS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

ANISO-PRESSURE	BAROSTAT	COLLISION
COMPRESS	FRICTION	FRICTION-SCALING
TAU-PRESSURE	TAU-TEMPERATURE	THERMOSTAT
VOLUME-MOVE	VOLUME-SCALE	VOLUME-TRIAL

TRANSITION STATE KEYWORDS
^^^^^^^^^^^^^^^^^^^^^^^^^

DIVERGE	GAMMAMIN	REDUCE
SADDLEPOINT

DISTANCE GEOMETRY KEYWORDS
^^^^^^^^^^^^^^^^^^^^^^^^^^

TRIAL-DISTANCE	TRIAL-DISTRIBUTION

VIBRATIONAL ANALYSIS KEYWORDS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

IDUMP	VIB-ROOTS	VIB-TOLERANCE

IMPLICIT SOLVATION KEYWORDS
^^^^^^^^^^^^^^^^^^^^^^^^^^^

BORN-RADIUS	GK-RADIUS	GKC
GKR	SOLVENT-PRESSURE	SURFACE-TENSION

POISSON-BOLTZMANN KEYWORDS
^^^^^^^^^^^^^^^^^^^^^^^^^^

APBS-AGRID	APBS-BCFL	APBS-CGCENT
APBS-CGRID	APBS-DIME	APBS-FGCENT
APBS-FGRID	APBS-GCENT	APBS-GRID
APBS-ION	APBS-MG-AUTO	APBS-MG-MANUAL
APBS-PDIE	APBS-RADII	APBS-SDENS
APBS-SDIE	APBS-SMIN	APBS-SRAD
APBS-SRFM	APBS-SWIN

MATHEMATICAL ALGORITHM KEYWORDS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

FFT-PACKAGE	RANDOMSEED

PARALLELIZATION KEYWORDS
^^^^^^^^^^^^^^^^^^^^^^^^

OPENMP-THREADS

FREE ENERGY PERTURBATION KEYWORDS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

CHG-LAMBDA	DPL-LAMBDA	LAMBDA
LIGAND	MPOLE-LAMBDA	MUTATE
POLAR-LAMBDA	VDW-ANNIHILATE	VDW-LAMBDA

PARTIAL STRUCTURE KEYWORDS
^^^^^^^^^^^^^^^^^^^^^^^^^^

ACTIVE	GROUP	GROUP-INTER
GROUP-INTRA	GROUP-MOLECULE	GROUP-SELECT
INACTIVE

CONSTRAINT & RESTRAINT KEYWORDS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

BASIN	ENFORCE-CHIRALITY	RATTLE
RATTLE-DISTANCE	RATTLE-EPS	RATTLE-LINE
RATTLE-ORIGIN	RATTLE-PLANE	RESTRAIN-ANGLE
RESTRAIN-DISTANCE	RESTRAIN-GROUPS	RESTRAIN-POSITION
RESTRAIN-TORSION	SPHERE	WALL

PARAMETER FITTING KEYWORDS
^^^^^^^^^^^^^^^^^^^^^^^^^^

FIT-ANGLE	FIT-BOND	FIT-OPBEND
FIT-STRBND	FIT-TORSION	FIT-UREY
FIX-ANGLE	FIX-BOND	FIX-DIPOLE
FIX-MONOPOLE	FIX-OPBEND	FIX-QUADRUPOLE
FIX-STRBND	FIX-TORSION	FIX-UREY
POTENTIAL-ATOMS	POTENTIAL-FIT	POTENTIAL-OFFSET
POTENTIAL-SHELLS	POTENTIAL-SPACING	RESP-WEIGHT
RESPTYPE	TARGET-DIPOLE	TARGET-QUADRUPOLE

POTENTIAL SMOOTHING KEYWORDS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

DEFORM	DIFFUSE-CHARGE	DIFFUSE-TORSION
DIFFUSE-VDW	SMOOTHING

Description of Individual Keywords
----------------------------------

The following is an alphabetical list of the Tinker keywords along with a brief description of the action of each keyword and required or optional parameters that can be used to extend or modify each keyword. The format of possible modifiers, if any, is shown in brackets following each keyword.

.. index:: A-AXIS
.. _KEY-A-AXIS:

A-AXIS [real]
   Sets the value of the a-axis length for a crystal unit cell, or, equivalently, the X-axis length for a periodic box. The length value in Angstroms is listed after the keyword. Equivalent to the X-AXIS keyword.

.. index:: A-EXPTERM
.. _KEY-A-EXPTERM:

A-EXPTERM [real]
   Sets the value of the "A" premultiplier term in the Buckingham van der Waals function, i.e., the value of A in the formula Evdw = epsilon * { A exp[-B(Ro/R)] - C (Ro/R)6 }.

.. index:: ACTIVE
.. _KEY-ACTIVE:

ACTIVE [integer list]
   Sets the list of active atoms during a Tinker computation. Individual potential energy terms are computed when at least one atom involved in the term is active. For Cartesian space calculations, active atoms are those allowed to move. For torsional space calculations, rotations are allowed when all atoms on one side of the rotated bond are active. Multiple ACTIVE lines can be present in the keyfile and are treated cumulatively.  On each line the keyword can be followed by one or more atom numbers or atom ranges. The presence of any ACTIVE keyword overrides any INACTIVE keywords in the keyfile.

.. index:: ACTIVE-SPHERE
.. _KEY-ACTIVE-SPHERE:

ACTIVE-SPHERE [4 reals, or 1 integer & 1 real]
   Provides an alternative to the ACTIVE and INACTIVE keywords for specification of subsets of active atoms. If four real number modifiers are provided, the first three are taken as X-, Y- and Z-coordinates and the fourth is the radius of a sphere centered at these coordinates. In this case, all atoms within the sphere at the start of the calculation are active throughout the calculation, while all other atoms are inactive. Similarly if one integer and real number are given, an "active" sphere with radius set by the real is centered on the system atom with atom number given by the integer modifier. Multiple SPHERE keyword lines can be present in a single keyfile, and the list of active atoms specified by the spheres is cumulative.

.. index:: ALPHA
.. _KEY-ALPHA:

ALPHA [real]
   Sets the value of the alpha angle of a crystal unit cell, i.e., the angle between the b-axis and c-axis of a unit cell, or, equivalently, the angle between the Y-axis and Z-axis of a periodic box. The default value in the absence of the ALPHA keyword is 90 degrees.

.. index:: ANGANG
.. _KEY-ANGANG:

ANGANG [1 integer & 3 reals]
   Provides the values for a single angle-angle cross term potential parameter. The integer modifier is the atom class of the central atom in the coupled angles. The real number modifiers give the force constant values for individual angles with 0, 1 or 2 terminal hydrogen atoms, respectively. The default units for the force constant are kcal/mole/radian^2, but this can be controlled via the ANGANGUNIT keyword.

.. index:: ANGANGTERM
.. _KEY-ANGANGTERM:

ANGANGTERM [NONE/ONLY]
   Controls use of the angle-angle cross term potential energy. In the absence of a modifying option, this keyword turns on use of the potential. The NONE option turns off use of this potential energy term. The ONLY option turns off all potential energy terms except for this one.

.. index:: ANGANGUNIT
.. _KEY-ANGANGUNIT:

ANGANGUNIT [real]
   Sets the scale factor needed to convert the energy value computed by the angle-angle cross term potential into units of kcal/mole. The correct value is force field dependent and typically provided in the header of the master force field parameter file. The default of (Pi/180)^2 = 0.0003046 is used, if the ANGANGUNIT keyword is not given in the force field parameter file or the keyfile.

.. index:: ANGCFLUX
.. _KEY-ANGCFLUX:

ANGCFLUX [3 integers & 4 reals]
   Provides the values for a single angle bending charge flux parameter. The integer modifiers give the atom class numbers for the three kinds of atoms involved in the angle which is to be defined. The first two real modifiers are the angle deviation scale factors for the two included bonds in electrons/radian. The second two modifiers are the bond deviation scale factors for the two included bonds in electrons/Angstrom.

.. index:: ANGLE
.. _KEY-ANGLE:

ANGLE [3 integers & 4 reals]
   Provides the values for a single bond angle bending parameter. The integer modifiers give the atom class numbers for the three kinds of atoms involved in the angle which is to be defined. The real number modifiers give the force constant value for the angle and up to three ideal bond angles in degrees. In most cases only one ideal bond angle is given, and that value is used for all occurrences of the specified bond angle. If all three ideal angles are given, the values apply when the central atom of the angle is attached to 0, 1 or 2 additional hydrogen atoms, respectively. This "hydrogen environment" option is provided to implement the corresponding feature of Allinger's MM force fields. The default units for the force constant are kcal/mole/radian^2, but this can be controlled via the ANGLEUNIT keyword.

.. index:: ANGLE-CUBIC
.. _KEY-ANGLE-CUBIC:

ANGLE-CUBIC [real]
   Sets the value of the cubic term in the Taylor series expansion form of the bond angle bending potential energy. The real number modifier gives the value of the coefficient as a multiple of the quadratic coefficient. This term multiplied by the angle bending energy unit conversion factor, the force constant, and the cube of the deviation of the bond angle from its ideal value gives the cubic contribution to the angle bending energy. The default value in the absence of the ANGLE-CUBIC keyword is zero; i.e., the cubic angle bending term is omitted.

.. index:: ANGLE-PENTIC
.. _KEY-ANGLE-PENTIC:

ANGLE-PENTIC [real]
   Sets the value of the fifth power term in the Taylor series expansion form of the bond angle bending potential energy. The real number modifier gives the value of the coefficient as a multiple of the quadratic coefficient. This term multiplied by the angle bending energy unit conversion factor, the force constant, and the fifth power of the deviation of the bond angle from its ideal value gives the pentic contribution to the angle bending energy. The default value in the absence of the ANGLE-PENTIC keyword is zero; i.e., the pentic angle bending term is omitted.

.. index:: ANGLE-QUARTIC
.. _KEY-ANGLE-QUARTIC:

ANGLE-QUARTIC [real]
   Sets the value of the quartic term in the Taylor series expansion form of the bond angle bending potential energy. The real number modifier gives the value of the coefficient as a multiple of the quadratic coefficient. This term multiplied by the angle bending energy unit conversion factor, the force constant, and the forth power of the deviation of the bond angle from its ideal value gives the quartic contribution to the angle bending energy. The default value in the absence of the ANGLE-QUARTIC keyword is zero; i.e., the quartic angle bending term is omitted.

.. index:: ANGLE-SEXTIC
.. _KEY-ANGLE-SEXTIC:

ANGLE-SEXTIC [real]
   Sets the value of the sixth power term in the Taylor series expansion form of the bond angle bending potential energy. The real number modifier gives the value of the coefficient as a multiple of the quadratic coefficient. This term multiplied by the angle bending energy unit conversion factor, the force constant, and the sixth power of the deviation of the bond angle from its ideal value gives the sextic contribution to the angle bending energy. The default value in the absence of the ANGLE-SEXTIC keyword is zero; i.e., the sextic angle bending term is omitted.

.. index:: ANGLE3
.. _KEY-ANGLE3:

ANGLE3 [3 integers & 4 reals]
   Provides the values for a single bond angle bending parameter specific to atoms in 3-membered rings. The integer modifiers give the atom class numbers for the three kinds of atoms involved in the angle which is to be defined. The real number modifiers give the force constant value for the angle and up to three ideal bond angles in degrees. If all three ideal angles are given, the values apply when the central atom of the angle is attached to 0, 1 or 2 additional hydrogen atoms, respectively. The default units for the force constant are kcal/mole/radian^2, but this can be controlled via the ANGLEUNIT keyword. If any ANGLE3 keywords are present, either in the master force field parameter file or the keyfile, then Tinker requires that special ANGLE3 parameters be given for all angles in 3-membered rings. In the absence of any ANGLE3 keywords, standard ANGLE parameters will be used for bonds in 3-membered rings.

.. index:: ANGLE4
.. _KEY-ANGLE4:

ANGLE4 [3 integers & 4 reals]
   Provides the values for a single bond angle bending parameter specific to atoms in 4-membered rings. The integer modifiers give the atom class numbers for the three kinds of atoms involved in the angle which is to be defined. The real number modifiers give the force constant value for the angle and up to three ideal bond angles in degrees. If all three ideal angles are given, the values apply when the central atom of the angle is attached to 0, 1 or 2 additional hydrogen atoms, respectively. The default units for the force constant are kcal/mole/radian^2, but this can be controlled via the ANGLEUNIT keyword. If any ANGLE4 keywords are present, either in the master force field parameter file or the keyfile, then Tinker requires that special ANGLE4 parameters be given for all angles in 4-membered rings. In the absence of any ANGLE4 keywords, standard ANGLE parameters will be used for bonds in 4-membered rings.

.. index:: ANGLE5
.. _KEY-ANGLE5:

ANGLE5 [3 integers & 4 reals]
   Provides the values for a single bond angle bending parameter specific to atoms in 5-membered rings. The integer modifiers give the atom class numbers for the three kinds of atoms involved in the angle which is to be defined. The real number modifiers give the force constant value for the angle and up to three ideal bond angles in degrees. If all three ideal angles are given, the values apply when the central atom of the angle is attached to 0, 1 or 2 additional hydrogen atoms, respectively. The default units for the force constant are kcal/mole/radian^2, but this can be controlled via the ANGLEUNIT keyword. If any ANGLE5 keywords are present, either in the master force field parameter file or the keyfile, then Tinker requires that special ANGLE5 parameters be given for all angles in 5-membered rings. In the absence of any ANGLE5 keywords, standard ANGLE parameters will be used for bonds in 5-membered rings.

.. index:: ANGLEF
.. _KEY-ANGLEF:

ANGLEF [3 integers & 3 reals]
   Provides the values for a single bond angle bending parameter for a SHAPES-style Fourier potential function. The integer modifiers give the atom class numbers for the three kinds of atoms involved in the angle which is to be defined. The real number modifiers give the force constant value for the angle, the angle shift in degrees, and the periodicity value. Note that the force constant should be given as the "harmonic" value and not the native Fourier value. The default units for the force constant are kcal/mole/radian^2, but this can be controlled via the ANGLEUNIT keyword.

.. index:: ANGLEP
.. _KEY-ANGLEP:

ANGLEP [3 integers & 3 reals]
   Provides the values for a single projected in-plane bond angle bending parameter. The integer modifiers give the atom class numbers for the three kinds of atoms involved in the angle which is to be defined. The real number modifiers give the force constant value for the angle and up to two ideal bond angles in degrees. In most cases only one ideal bond angle is given, and that value is used for all occurrences of the specified bond angle. If all two ideal angles are given, the values apply when the central atom of the angle is attached to 0 or 1 additional hydrogen atoms, respectively. This "hydrogen environment" option is provided to implement the corresponding feature of Allinger's MM force fields. The default units for the force constant are kcal/mole/radian2, but this can be controlled via the ANGLEUNIT keyword.

.. index:: ANGLETERM
.. _KEY-ANGLETERM:

ANGLETERM [NONE/ONLY]
   Controls use of the bond angle bending potential energy term. In the absence of a modifying option, this keyword turns on use of the potential. The NONE option turns off use of this potential energy term. The ONLY option turns off all potential energy terms except for this one.

.. index:: ANGLEUNIT
.. _KEY-ANGLEUNIT:

ANGLEUNIT [real]
   Sets the scale factor needed to convert the energy value computed by the bond angle bending potential into units of kcal/mole. The correct value is force field dependent and typically provided in the header of the master force field parameter file. The default value of (Pi/180)^2 = 0.0003046 is used, if the ANGLEUNIT keyword is not given in the force field parameter file or the keyfile.

.. index:: ANGMAX
.. _KEY-ANGMAX:

ANGMAX [real]
   Set the maximum permissible angle between the current optimization search direction and the negative of the gradient direction. If this maximum angle value is exceeded, the optimization routine will note an error condition and may restart from the steepest descent direction. The default value in the absence of the ANGMAX keyword is usually 88 degrees for conjugate gradient methods and 180 degrees (i.e., ANGMAX is disabled) for variable metric optimizations.

.. index:: ANGTORS
.. _KEY-ANGTORS:

ANGTORS [4 integers & 6 reals]
   Provides the values for a single bond angle bending-torsional angle parameter. The integer modifiers give the atom class numbers for the four kinds of atoms involved in the torsion and its contained angles. The real number modifiers give the force constant values for both angles coupled with 1-, 2- and 3-fold torsional terms. The default units for the force constants are kcal/mole/radian, but this can be controlled via the ANGTORUNIT keyword.

.. index:: ANGTORTERM
.. _KEY-ANGTORTERM:

ANGTORTERM [NONE/ONLY]
   Controls use of the angle bending-torsional angle cross term. In the absence of a modifying option, this keyword turns on use of the potential. The NONE option turns off use of this potential energy term. The ONLY option turns off all potential energy terms except for this one.

.. index:: ANGTORUNIT
.. _KEY-ANGTORUNIT:

ANGTORUNIT [real]
   Sets the scale factor needed to convert the energy value computed by the angle bending-torsional angle cross term into units of kcal/mole. The correct value is force field dependent and typically provided in the header of the master force field parameter file. The default value of (Pi/180) = 0.0174533 is used, if the ANGTORUNIT keyword is not given in the force field parameter file or the keyfile.

.. index:: ANISO-PRESSURE
.. _KEY-ANISO-PRESSURE:

ANISO-PRESSURE
   Invokes use of full anisotropic pressure during dynamics simulations. When using this option, the three axis lengths and axis angles vary separately in response to the pressure tensor. The default, in the absence of the keyword, is isotropic pressure based on the average of the diagonal of the pressure tensor.

.. index:: APBS-AGRID
.. _KEY-APBS-AGRID:

APBS-AGRID [3 reals]
   Sets grid spacing in Angstroms along the X-, Y- and Z-axes which are passed on to the APBS interface for use in Poisson-Boltzmann calculations.

.. index:: APBS-BCFL
.. _KEY-APBS-BCFL:

APBS-BCFL [ZERO/SDH/MDH]
   Chooses the type of boundary conditions to be used when performing Poisson-Boltzmann calculations. The ZERO modifier denotes a zero potential at the boundary, while SDH and MDH are single and multiple Debye-Huckel conditions. The default setting in the absence of the BCFL keyword is to use the MDH boundary conditions.

.. index:: APBS-CGCENT
.. _KEY-APBS-CGCENT:

APBS-CGCENT [3 reals]
   Sets the coarse grid center as X-, Y- and Z-axis coordinates for an APBS Poisson-Boltzmann calculation when using a "focusing" calculation as activated via the APBS-MG-AUTO keyword.

.. index:: APBS-CGRID
.. _KEY-APBS-CGRID:

APBS-CGRID [3 reals]
   Sets the coarse grid dimensions along the X-, Y- and Z-axes for an APBS Poisson-Boltzmann calculation when using a "focusing" calculation as activated via the APBS-MG-AUTO keyword.

.. index:: APBS-DIME
.. _KEY-APBS-DIME:

APBS-DIME [3 integers]
   Specifies the number of grid points along the X-, Y- and Z-axes for APBS Poisson-Boltzmann calculations. This keyword gives final, custom control over the grid dimensions that are usually set via the APBS-GRID keyword. When using traceless atomic quadrupole moments, all grid dimensions will be forced to be equal.

.. index:: APBS-FGCENT
.. _KEY-APBS-FGCENT:

APBS-FGCENT [3 reals]
   Sets the fine grid center as X-, Y- and Z-axis coordinates for an APBS Poisson-Boltzmann calculation when using a "focusing" calculation as activated via the APBS-MG-AUTO keyword.

.. index:: APBS-FGRID
.. _KEY-APBS-FGRID:

APBS-FGRID [3 reals]
   Sets the fine grid dimensions along the X-, Y- and Z-axes for an APBS Poisson-Boltzmann calculation when using a "focusing" calculation as activated via the APBS-MG-AUTO keyword.

.. index:: APBS-GCENT
.. _KEY-APBS-GCENT:

APBS-GCENT [3 reals]
   Sets grid dimensions along the X-, Y- and Z-axes which are passed on to the Tinker APBS interface for use in Poisson-Boltzmann calculations.

.. index:: APBS-GRID
.. _KEY-APBS-GRID:

APBS-GRID [3 integers]
   Sets the number of grid points along the X-, Y- and Z-axes when performing an APBS Poisson-Boltzmann calculation. The default values in the absence of the APBS-GRID keyword are chosen as the nearest integers that provide a 0.5 Angstrom grid spacing along each axis. When using traceless atomic quadrupole moments, all grid dimensions will be forced to be equal.

.. index:: APBS-ION
.. _KEY-APBS-ION:

APBS-ION [3 reals]
   Specifies the mobile ion concentration for use during APBS Poisson-Boltzmann calculations. The real modifiers are the charge of the ion species in electrons, the molar ion concentration, and the radius in Angstroms of the ion species. The default in the absence of the APBS-ION keyword is to not include any mobile ions via setting the concentration to zero.

.. index:: APBS-MG-AUTO
.. _KEY-APBS-MG-AUTO:

APBS-MG-AUTO
   Specifies a "focusing" multigrid APBS Poisson-Boltzmann calculation where a series of single-point calculations are used to successively zoom in on a region of interest in a system. It is basically an automated version of the default MG-MANUAL mode, which is designed for easier use.

.. index:: APBS-MG-MANUAL
.. _KEY-APBS-MG-MANUAL:

APBS-MG-MANUAL
   Specifies a manually configured single-point multigrid APBS Poisson-Boltzmann calculation without focusing or additional refinement. This mode offers the most control of APBS parameters to the user. This is the default mode for APBS calculations unless the APBS-MG-MANUAL keyword is present.

.. index:: APBS-PDIE
.. _KEY-APBS-PDIE:

APBS-PDIE [real]
   Specifies the dielectric constant of the solute molecule for APBS Poisson-Boltzmann calculations. This is often a value between 2 and 20, where lower values consider only electronic polarization and higher values account for additional polarization due to intramolecular motion. The default in the absence of the APBS-PDIE keyword is to set the solute dielectric constant to 1.0.

.. index:: APBS-RADII
.. _KEY-APBS-RADII:

APBS-RADII [VDW/MACROMODEL/BONDI/TOMASI]
   Specifies the atomic radii values to be used during APBS Poisson-Boltzmann calculations. The default in the absence o the APBS-RADII keyword is to use BONDI radii.

.. index:: APBS-SDENS
.. _KEY-APBS-SDENS:

APBS-SDENS [real]
   Sets the number of quadrature points per square Angstrom to use in surface area terms during APSB Poisson-Boltzmann calculations. The default in the absence of the APBS-SDENS keyword is to use a value of 10.0, although this keyword is ignored it APBS-SRAD is zero.

.. index:: APBS-SDIE
.. _KEY-APBS-SDIE:

APBS-SDIE [real]
   Specifies the dielectric constant of the solvent for APBS Poisson-Boltzmann calculations. Bulk water is usually modeled with a dielectric constant of 78 to 80. The default in the absence of the APBS-SDIE keyword is to set the solvent dielectric constant to 78.3.

.. index:: APBS-SMIN
.. _KEY-APBS-SMIN:

APBS-SMIN [real]
   Sets an offset buffer distance in Angstroms to be added to the width of the solute molecule in determination of the grid dimension and spacing during an APBS Poisson-Boltzmann calculation. The default in the absence of the APBS-SMIN keyword is to use a value of 3.0 Angstroms.

.. index:: APBS-SRAD
.. _KEY-APBS-SRAD:

APBS-SRAD [real]
   Provides the radius in Angstroms of solvent molecules to be used during APBS Poisson-Boltzmann calculations. This value is usually set to 1.4 for a water-like molecular surface, and set to zero for a van der Waals surface. The default in the absence of the APBS-SRAD keyword is to use a value of 1.4 Angstroms.

.. index:: APBS-SRFM
.. _KEY-APBS-SRFM:

APBS-SRFM [MOL/SMOL/SPL2/SPL4]
   Specifies the model used to construct the dielectric and ion-accessibility coefficients during APBS Poisson-Boltzmann calculations. The MOL modifier sets the dielectric coefficient based on the molecular surface, while SMOL uses a smoothed molecular surface. The SPL2 and SPL4 models use a cubic spline surface and a 7th order polynomial, respectively. The default in the absence of the APBS-SRFM keyword is to use the SPL4 model.

.. index:: APBS-SWIN
.. _KEY-APBS-SWIN:

APBS-SWIN [real]
   Specifies the spline window width in Angstroms for surface definitions during APBS Poisson-Boltzmann calculations. The default in the absence of the APBS-SWIN keyword is to use a value of 0.3 Angstroms.

.. index:: ATOM
.. _KEY-ATOM:

ATOM [2 integers, name, quoted string, integer, real & integer]
   Provides the values needed to define a single force field atom type. The first two integer modifiers denote the atom type and class numbers. If the type and class are identical, only a single integer value is required. The next modifier is a three-character atom name, followed by an 24-character or less atom description contained in single quotes. The next two modifiers are the atomic number and atomic mass. The final integer modifier is the "valence" of the atom, defined as the expected number of attached or bonded atoms.

.. index:: AUX-TAUTEMP
.. _KEY-AUX-TAUTEMP:

AUX-TAUTEMP [real]
   Sets the coupling time in picoseconds for the temperature bath coupling used to control the auxiliary thermostat temperature value when using the iELSCF induced dipole method. A default value of 0.1 is used for AUX-TAUTEMP in the absence of the keyword.

.. index:: AUX-TEMP
.. _KEY-AUX-TEMP:

AUX-TEMP [real]
   Sets the target temperature used for the auxiliary control variable when using the iELSCF induced dipole method. A default value of 100000.0 is used for AUX-TEMP in the absence of the keyword.

.. index:: B-AXIS
.. _KEY-B-AXIS:

B-AXIS [real]
   Sets the value of the b-axis length for a crystal unit cell, or, equivalently,  the Y-axis length for a periodic box. The length value in Angstroms is listed after the keyword. If the keyword is absent, the b-axis length is set equal to the a-axis length. Equivalent to the Y-AXIS keyword.

.. index:: B-EXPTERM
.. _KEY-B-EXPTERM:

B-EXPTERM [real]
   Sets the value of the "B" exponential factor in the Buckingham van der Waals function, i.e., the value of B in the formula Evdw = epsilon * { A exp[-B(Ro/R)] - C (Ro/R)6 }.

.. index:: BAROSTAT
.. _KEY-BAROSTAT:

BAROSTAT [BERENDSEN]
   Selects a barostat algorithm for use during molecular dynamics. At present only one modifier is available, a Berendsen bath coupling method. The default in the absence of the BAROSTAT keyword is to use the BERENDSEN algorithm.

.. index:: BASIN
.. _KEY-BASIN:

BASIN [2 reals]
   Presence of this keyword turns on a "basin" restraint potential function that serves to drive the system toward a compact structure. The actual function is a Gaussian of the form Ebasin = epsilon * A exp[-B R^2], summed over all pairs of atoms where R is the distance between atoms. The A and B values are the depth and width parameters given as modifiers to the BASIN keyword. This potential is currently used to control the degree of expansion during potential energy smooth procedures through the use of shallow, broad basins.

.. index:: BEEMAN-MIXING
.. _KEY-BEEMAN-MIXING:

BEEMAN-MIXING [integer]
   Sets the "mixing" coefficient between old and new forces in position and velocity updates when using the Beeman integrator. The original algorithm of Beeman uses a value of 6. The default value in the absence of the BEEMAN-MIXING keyword is to use 8, which corresponds to the "Better Beeman" algorithm proposed by Bernie Brooks.

.. index:: BETA
.. _KEY-BETA:

BETA [real]
   Sets the value of the ? angle of a crystal unit cell, i.e., the angle between the a-axis and c-axis of a unit cell, or, equivalently, the angle between the X-axis and Z-axis of a periodic box. The default value in the absence of the BETA keyword is to set the beta angle equal to the alpha angle as given by the keyword ALPHA.

.. index:: BIOTYPE
.. _KEY-BIOTYPE:

BIOTYPE [integer, name, quoted string & integer]
   Provides the values to define the correspondence between a single biopolymer atom type and its force field atom type.

.. index:: BOND
.. _KEY-BOND:

BOND [2 integers & 2 reals]
   Provides the values for a single bond stretching parameter. The integer modifiers give the atom class numbers for the two kinds of atoms involved in the bond which is to be defined. The real number modifiers give the force constant value for the bond and the ideal bond length in Angstroms. The default units for the force constant are kcal/mole/Ang^2, but this can be controlled via the BONDUNIT keyword.

.. index:: BOND-CUBIC
.. _KEY-BOND-CUBIC:

BOND-CUBIC [real]
   Sets the value of the cubic term in the Taylor series expansion form of the bond stretching potential energy. The real number modifier gives the value of the coefficient as a multiple of the quadratic coefficient. This term multiplied by the bond stretching energy unit conversion factor, the force constant, and the cube of the deviation of the bond length from its ideal value gives the cubic contribution to the bond stretching energy. The default value in the absence of the BOND-CUBIC keyword is zero; i.e., the cubic bond stretching term is omitted.

.. index:: BOND-QUARTIC
.. _KEY-BOND-QUARTIC:

BOND-QUARTIC [real]
   Sets the value of the quartic term in the Taylor series expansion form of the bond stretching potential energy. The real number modifier gives the value of the coefficient as a multiple of the quadratic coefficient. This term multiplied by the bond stretching energy unit conversion factor, the force constant, and the forth power of the deviation of the bond length from its ideal value gives the quartic contribution to the bond stretching energy. The default value in the absence of the BOND-QUARTIC keyword is zero; i.e., the quartic bond stretching term is omitted.

.. index:: BOND3
.. _KEY-BOND3:

BOND3 [2 integers & 2 reals]
   Provides the values for a single bond stretching parameter specific to atoms in 3-membered rings. The integer modifiers give the atom class numbers for the two kinds of atoms involved in the bond which is to be defined. The real number modifiers give the force constant value for the bond and the ideal bond length in Angstroms. The default units for the force constant are kcal/mole/Ang^2, but this can be controlled via the BONDUNIT keyword. If any BOND3 keywords are present, either in the master force field parameter file or the keyfile, then Tinker requires that special BOND3 parameters be given for all bonds in 3-membered rings. In the absence of any BOND3 keywords, standard BOND parameters will be used for bonds in 3-membered rings.

.. index:: BOND4
.. _KEY-BOND4:

BOND4 [2 integers & 2 reals]
   Provides the values for a single bond stretching parameter specific to atoms in 4-membered rings. The integer modifiers give the atom class numbers for the two kinds of atoms involved in the bond which is to be defined. The real number modifiers give the force constant value for the bond and the ideal bond length in Angstroms. The default units for the force constant are kcal/mole/Ang^2, but this can be controlled via the BONDUNIT keyword. If any BOND4 keywords are present, either in the master force field parameter file or the keyfile, then Tinker requires that special BOND4 parameters be given for all bonds in 4-membered rings. In the absence of any BOND4 keywords, standard BOND parameters will be used for bonds in 4-membered rings

.. index:: BOND5
.. _KEY-BOND5:

BOND5 [2 integers & 2 reals]
   Provides the values for a single bond stretching parameter specific to atoms in 5-membered rings. The integer modifiers give the atom class numbers for the two kinds of atoms involved in the bond which is to be defined. The real number modifiers give the force constant value for the bond and the ideal bond length in Angstroms. The default units for the force constant are kcal/mole/Ang^2, but this can be controlled via the BONDUNIT keyword. If any BOND5 keywords are present, either in the master force field parameter file or the keyfile, then Tinker requires that special BOND5 parameters be given for all bonds in 5-membered rings. In the absence of any BOND5 keywords, standard BOND parameters will be used for bonds in 5-membered rings

.. index:: BONDTERM
.. _KEY-BONDTERM:

BONDTERM [NONE/ONLY]
   Controls use of the bond stretching potential energy term. In the absence of a modifying option, this keyword turns on use of the potential. The NONE option turns off use of this potential energy term. The ONLY option turns off all potential energy terms except for this one.

.. index:: BONDTYPE
.. _KEY-BONDTYPE:

BONDTYPE [HARMONIC/MORSE]
   Chooses the functional form of the bond stretching potential. The HARMONIC option selects a Taylor series expansion containing terms from harmonic through quartic. The MORSE option selects a Morse potential fit to the ideal bond length and stretching force constant parameter values. The default is to use the HARMONIC potential.

.. index:: BONDUNIT
.. _KEY-BONDUNIT:

BONDUNIT [real]
   Sets the scale factor needed to convert the energy value computed by the bond stretching potential into units of kcal/mole. The correct value is force field dependent and typically provided in the header of the master force field parameter file. The default value of 1.0 is used, if the BONDUNIT keyword is not given in the force field parameter file or the keyfile.

.. index:: BORN-RADIUS
.. _KEY-BORN-RADIUS:

BORN-RADIUS [ONION/STILL/HCT/OBC/ACE/GRYCUK/PERFECT]
   Sets the algorithm used for computation of Born radii. The default behavior is to set BORN-RADIUS the same as the SOLVATE keyword, when possible. For Generalized Kirkwood models, the default value is set to GRYCUK.

.. index:: C-AXIS
.. _KEY-C-AXIS:

C-AXIS [real]
   Sets the value of the C-axis length for a crystal unit cell, or, equivalently, the Z-axis length for a periodic box. The length value in Angstroms is listed after the keyword. If the keyword is absent, the C-axis length is set equal to the A-axis length. Equivalent to the Z-AXIS keyword.

.. index:: C-EXPTERM
.. _KEY-C-EXPTERM:

C-EXPTERM [real]
   Sets the value of the "C" dispersion multiplier in the Buckingham van der Waals function, i.e., the value of C in the formula Evdw = epsilon * { A*exp[-B(Ro/R)] - C*(Ro/R)^6 }.

.. index:: CAPPA
.. _KEY-CAPPA:

CAPPA [real]
   Sets the normal termination criterion for the line search phase of Tinker optimization routines. The line search exits successfully if the ratio of the current gradient projection on the line to the projection at the start of the line search falls below the value of CAPPA. A default value of 0.1 is used in the absence of the CAPPA keyword.

.. index:: CHARGE
.. _KEY-CHARGE:

CHARGE [1 integer & 1 real]
   Provides a value for a single atomic partial charge electrostatic parameter. The integer modifier, if positive, gives the atom type number for which the charge parameter is to be defined. Note that charge parameters are given for atom types, not atom classes. If the integer modifier is negative, then the parameter value to follow applies only to the individual atom whose atom number is the negative of the modifier. The real number modifier gives the values of the atomic partial charge in electrons.

.. index:: CHARGE-CUTOFF
.. _KEY-CHARGE-CUTOFF:

CHARGE-CUTOFF [real]
   Sets the cutoff distance value in Angstroms for charge-charge electrostatic potential energy interactions. The energy for any pair of sites beyond the cutoff distance will be set to zero. Other keywords can be used to select a smoothing scheme near the cutoff distance. The default cutoff distance in the absence of the CHG-CUTOFF keyword is infinite for nonperiodic systems and 9.0 for periodic systems.

.. index:: CHARGE-LIST
.. _KEY-CHARGE-LIST:

CHARGE-LIST
   Turns on the use of pairwise neighbor lists for partial charge electrostatics. This method will yield identical energetic results to the standard double loop method.

.. index:: CHARGE-TAPER
.. _KEY-CHARGE-TAPER:

CHARGE-TAPER [real]
   Modifies the cutoff window for charge-charge electrostatic potential energy interactions. It is similar in form and action to the TAPER keyword, except that its value applies only to the charge-charge potential. The default value in the absence of the CHG-TAPER keyword is to begin the cutoff window at 0.65 of the corresponding cutoff distance.

.. index:: CHARGETERM
.. _KEY-CHARGETERM:

CHARGETERM [NONE/ONLY]
   Controls use of the charge-charge potential energy term between pairs of atomic partial charges. In the absence of a modifying option, this keyword turns on use of the potential. The NONE option turns off use of this potential energy term. The ONLY option turns off all potential energy terms except for this one.

.. index:: CHARGETRANSFER
.. _KEY-CHARGETRANSFER:

CHARGETRANSFER [SEPARATE/COMBINED]
   Chooses the formulation used for the charge transfer potential energy function. The SEPARATE method includes separate terms for charge transfer in both directions between two atomic sites. The COMBINED model uses a single term to account for the total charge transfer interaction between two sites. The default value in the absence of the CHARGETRANSFER keyword is to use the SEPARATE expression to compute the charge transfer potential.

.. index:: CHG-11-SCALE
.. _KEY-CHG-11-SCALE:

CHG-11-SCALE [real]
   Provides a multiplicative scale factor that is applied to charge-charge electrostatic interactions between self-atoms. These interactions are usually to be ignored, but this value is used in certain cases involving infinite polymers or atoms using the same "neighbor generating" site. The default value of 0.0 is used, if the CHG-11-SCALE keyword is not given in either the parameter file or the keyfile.

.. index:: CHG-12-SCALE
.. _KEY-CHG-12-SCALE:

CHG-12-SCALE [real]
   Provides a multiplicative scale factor that is applied to charge-charge electrostatic interactions between 1-2 connected atoms, i.e., atoms that are directly bonded. The default value of 0.0 is used, if the CHG-12-SCALE keyword is not given in either the parameter file or the keyfile.

.. index:: CHG-13-SCALE
.. _KEY-CHG-13-SCALE:

CHG-13-SCALE [real]
   Provides a multiplicative scale factor that is applied to charge-charge electrostatic interactions between 1-3 connected atoms, i.e., atoms separated by two covalent bonds. The default value of 0.0 is used, if the CHG-13-SCALE keyword is not given in either the parameter file or the keyfile.

.. index:: CHG-14-SCALE
.. _KEY-CHG-14-SCALE:

CHG-14-SCALE [real]
   Provides a multiplicative scale factor that is applied to charge-charge electrostatic interactions between 1-4 connected atoms, i.e., atoms separated by three covalent bonds. The default value of 1.0 is used, if the CHG-14-SCALE keyword is not given in either the parameter file or the keyfile.

.. index:: CHG-15-SCALE
.. _KEY-CHG-15-SCALE:

CHG-15-SCALE [real]
   Provides a multiplicative scale factor that is applied to charge-charge electrostatic interactions between 1-5 connected atoms, i.e., atoms separated by four covalent bonds. The default value of 1.0 is used, if the CHG-15-SCALE keyword is not given in either the parameter file or the keyfile.

.. index:: CHG-BUFFER
.. _KEY-CHG-BUFFER:

CHG-BUFFER [real]
   Specifies a fixed value which is added to the distance between pairs of atoms when applying Coulomb's law in the computation of partial charge electrostatic interactions. The default value of 0.0, which disables the use of the charge buffer mechanism, is used in the absence of the CHG-BUFFER keyword.

.. index:: CHGDPLTERM
.. _KEY-CHGDPLTERM:

CHGDPLTERM [NONE/ONLY]
   Controls use of the charge-dipole potential energy term between atomic partial charges and bond dipoles. In the absence of a modifying option, this keyword turns on use of the potential. The NONE option turns off use of this potential energy term. The ONLY option turns off all potential energy terms except for this one.

.. index:: CHGPEN
.. _KEY-CHGPEN:

CHGPEN [1 integer & 2 reals]
   Provides values for a single charge penetration parameter. The integer modifier, if positive, gives the atom class number for which the charge penetration is to be defined. If the integer modifier is negative, then the parameter values to follow apply only to the individual atom whose atom number is the negative of the modifier. The real number modifiers give the number of core electrons for the atomic site and the "alpha" exponent controlling the stregth of the charge penetration effect.

.. index:: CHGTRN
.. _KEY-CHGTRN:

CHGTRN [1 integer & 2 reals]
   Provides values for a single charge transfer parameter. The integer modifier, if positive, gives the atom class number for which the charge transfer is to be defined. If the integer modifier is negative, then the parameter values to follow apply only to the individual atom whose atom number is the negative of the modifier. The real number modifiers give the charge to be transferred for the atomic site and the "alpha" exponent controlling the damping of the charge transfer.

.. index:: CHGTRN-CUTOFF
.. _KEY-CHGTRN-CUTOFF:

CHGTRN-CUTOFF [real]
   Sets the cutoff distance value in Angstroms for charge transfer potential energy interactions. The energy for any pair of sites beyond the cutoff distance will be set to zero. Other keywords can be used to select a smoothing scheme near the cutoff distance. The default cutoff distance in the absence of the CHGTRN-CUTOFF keyword is 6.0 Angstroms.

.. index:: CHGTRN-TAPER
.. _KEY-CHGTRN-TAPER:

CHGTRN-TAPER [real]
   Modifies the cutoff window for charge transfer potential energy interactions. It is similar in form and action to the TAPER keyword, except that its value applies only to the charge transfer potential. The default value in the absence of the CHGTRN-TAPER keyword is to begin the cutoff window at 0.9 of the corresponding cutoff distance.

.. index:: CHGTRNTERM
.. _KEY-CHGTRNTERM:

CHGTRNTERM [NONE/ONLY]
   Controls use of the charge transfer potential energy term. In the absence of a modifying option, this keyword turns on use of the potential. The NONE option turns off use of this potential energy term. The ONLY option turns off all potential energy terms except for this one.

.. index:: COLLISION
.. _KEY-COLLISION:

COLLISION [real]
   Sets the value of the random collision frequency used in the Andersen stochastic collision dynamics thermostat. The supplied value has units of fs-1 atom-1 and is multiplied internal to Tinker by the time step in fs and N^2/3 where N is the number of atoms. The default value used in the absence of the COLLISION keyword is 0.1 which is appropriate for many systems but may need adjustment to achieve adequate temperature control without perturbing the dynamics.

.. index:: COMPRESS
.. _KEY-COMPRESS:

COMPRESS [real]
   Sets the value of the bulk solvent isothermal compressibility in 1/Atm for use during pressure computation and scaling in molecular dynamics computations. The default value used in the absence of the COMPRESS keyword is 0.000046, appropriate for water. This parameter serves as a scale factor for the Groningen-style pressure bath coupling time, and its exact value should not be of critical importance.

.. index:: CUTOFF
.. _KEY-CUTOFF:

CUTOFF [real]
   Sets the cutoff distance value for all nonbonded potential energy interactions. The energy for any of the nonbonded potentials of a pair of sites beyond the cutoff distance will be set to zero. Other keywords can be used to select a smoothing scheme near the cutoff distance, or to apply different cutoff distances to various nonbonded energy terms.

.. index:: D-EQUALS-P
.. _KEY-D-EQUALS-P:

D-EQUALS-P
   Forces the direct induction ("D") scale factors to be set equal to the polarization energy ("P") scale factors during computation of induced dipoles and the polarization potential energy. In the absence of the D-EQUALS-P keyword, these two sets of scale factors are independent and are allowed to be different.

.. index:: DEBUG
.. _KEY-DEBUG:

DEBUG
   Turns on printing of detailed information and intermediate values throughout the progress of a Tinker computation; not recommended for use with large structures or full potential energy functions since a summary of every individual interaction will usually be output.

.. index:: DEFORM
.. _KEY-DEFORM:

DEFORM [real]
   Sets the amount of diffusion equation-style smoothing that will be applied to the potential energy surface when using the SMOOTH force field. The real number option is equivalent to the "time" value in the original Piela, et al. formalism; the larger the value, the greater the smoothing. The default value is zero, meaning that no smoothing will be applied.

.. index:: DEGREES-FREEDOM
.. _KEY-DEGREES-FREEDOM:

DEGREES-FREEDOM [integer]
   Sets the number of degrees of freedom during a dynamics calculation. The integer modifier is used by thermostating methods and in other places as the number of degrees of freedom, overriding the value determined by the Tinker code at dynamics startup. In the absence of the keyword, the programs will automatically compute the correct value based on the number of atoms active during dynamics, bond or other constraints, and use of periodic boundary conditions.

.. index:: DELTA-HALGREN
.. _KEY-DELTA-HALGREN:

DELTA-HALGREN [real]
   Sets the value of the delta parameter in Halgren's buffered 14-7 vdw potential energy functional form. In the absence of the DELTA-HALGREN keyword, a default value of 0.07 is used.

.. index:: DEWALD
.. _KEY-DEWALD:

DEWALD
   Turns on the use of smooth particle mesh Ewald (PME) summation during computation of dispersion interactions in periodic systems. By default, in the absence of the DEWALD keyword, distance-based cutoffs are used for dispersion interactions.

.. index:: DEWALD-ALPHA
.. _KEY-DEWALD-ALPHA:

DEWALD-ALPHA [real]
   Sets the value of the Ewald coefficient which controls the width of the Gaussian screening charges during particle mesh Ewald summation for dispersion. In the absence of the DEWALD-ALPHA keyword, the EWALD-ALPHA is used, or a value is chosen which causes interactions outside the real-space cutoff to be below a fixed tolerance. For most standard applications of dispersion Ewald summation, the program default should be used.

.. index:: DEWALD-CUTOFF
.. _KEY-DEWALD-CUTOFF:

DEWALD-CUTOFF [real]
   Sets the value in Angstroms of the real-space distance cutoff for use during Ewald summation for dispersion interactions. By default, in the absence of the DEWALD-CUTOFF keyword, a value of 7.0 is used.

.. index:: DIELECTRIC
.. _KEY-DIELECTRIC:

DIELECTRIC [real]
   Sets the value of the bulk dielectric constant used to damp all electrostatic interaction energies for any of the Tinker electrostatic potential functions. The default value is force field dependent, but is usually equal to 1.0 (for Allinger's MM force fields the default is 1.5).

.. index:: DIELECTRIC-OFFSET
.. _KEY-DIELECTRIC-OFFSET:

DIELECTRIC-OFFSET [real]
   Sets the value in Angstroms of the dielectric offset constant by which solvation atomic radii are reduced during computation of Born radii. By default, in the absence of the DIELECTRIC-OFFSET keyword, a value of 0.09 is used.

.. index:: DIFFUSE-CHARGE
.. _KEY-DIFFUSE-CHARGE:

DIFFUSE-CHARGE [real]
   Used during potential function smoothing procedures to specify the effective diffusion coefficient to be applied to the smoothed form of the Coulomb's Law charge-charge potential function. In the absence of the DIFFUSE-CHARGE keyword, a default value of 3.5 is used.

.. index:: DIFFUSE-TORSION
.. _KEY-DIFFUSE-TORSION:

DIFFUSE-TORSION [real]
   Used during potential function smoothing procedures to specify the effective diffusion coefficient to be applied to the smoothed form of the torsion angle potential function. In the absence of the DIFFUSE-TORSION keyword, a default value of 0.0225 is used.

.. index:: DIFFUSE-VDW
.. _KEY-DIFFUSE-VDW:

DIFFUSE-VDW [real]
   Used during potential function smoothing procedures to specify the effective diffusion coefficient to be applied to the smoothed Gaussian approximation to the Lennard-Jones van der Waals potential function. In the absence of the DIFFUSE-VDW keyword, a default value of 1.0 is used.

.. index:: DIGITS
.. _KEY-DIGITS:

DIGITS [integer]
   Controls the number of digits of precision  output by Tinker in reporting potential energies and atomic coordinates. The allowed values for the integer modifier are 4, 6 and 8. Input values less than 4 will be set to 4, and those greater than 8 will be set to 8. Final energy values reported by most Tinker programs will contain the specified number of digits to the right of the decimal point. The number of decimal places to be output for atomic coordinates is generally two larger than the value of DIGITS. In the absence of the DIGITS keyword a default value of 4 is used, and  energies will be reported to 4 decimal places with coordinates to 6 decimal places.

.. index:: DIPOLE
.. _KEY-DIPOLE:

DIPOLE [2 integers & 2 reals]
   Provides the values for a single bond dipole electrostatic parameter. The integer modifiers give the atom type numbers for the two kinds of atoms involved in the bond dipole which is to be defined. The real number modifiers give the value of the bond dipole in Debyes and the position of the dipole site along the bond. If the bond dipole value is positive, then the first of the two atom types is the positive end of the dipole. For a negative bond dipole value, the first atom type listed is negative. The position along the bond is an optional modifier that gives the postion of the dipole site as a fraction between the first atom type (position=0) and the second atom type (position=1). The default for the dipole position in the absence of a specified value is 0.5, placing the dipole at the midpoint of the bond.

.. index:: DIPOLE-CUTOFF
.. _KEY-DIPOLE-CUTOFF:

DIPOLE-CUTOFF [real]
   Sets the cutoff distance value in Angstroms for bond dipole-bond dipole electrostatic potential energy interactions. The energy for any pair of bond dipole sites beyond the cutoff distance will be set to zero. Other keywords can be used to select a smoothing scheme near the cutoff distance. The default cutoff distance in the absence of the DPL-CUTOFF keyword is essentially infinite for nonperiodic systems and 10.0 for periodic systems.

.. index:: DIPOLE-TAPER
.. _KEY-DIPOLE-TAPER:

DIPOLE-TAPER [real]
   Modifies the cutoff windows for bond dipole-bond dipole electrostatic potential energy interactions. It is similar in form and action to the TAPER keyword, except that its value applies only to the vdw potential. The default value in the absence of the DPL-TAPER keyword is to begin the cutoff window at 0.75 of the dipole cutoff distance.

.. index:: DIPOLE3
.. _KEY-DIPOLE3:

DIPOLE3 [2 integers & 2 reals]
   Provides the values for a single bond dipole electrostatic parameter specific to atoms in 3-membered rings. The integer modifiers give the atom type numbers for the two kinds of atoms involved in the bond dipole which is to be defined. The real number modifiers give the value of the bond dipole in Debyes and the position of the dipole site along the bond. The default for the dipole position in the absence of a specified value is 0.5, placing the dipole at the midpoint of the bond. If any DIPOLE3 keywords are present, either in the master force field parameter file or the keyfile, then Tinker requires that special DIPOLE3 parameters be given for all bond dipoles in 3-membered rings. In the absence of any DIPOLE3 keywords, standard DIPOLE parameters will be used for bonds in 3-membered rings.

.. index:: DIPOLE4
.. _KEY-DIPOLE4:

DIPOLE4 [2 integers & 2 reals]
   Provides the values for a single bond dipole electrostatic parameter specific to atoms in 4-membered rings. The integer modifiers give the atom type numbers for the two kinds of atoms involved in the bond dipole which is to be defined. The real number modifiers give the value of the bond dipole in Debyes and the position of the dipole site along the bond. The default for the dipole position in the absence of a specified value is 0.5, placing the dipole at the midpoint of the bond. If any DIPOLE4 keywords are present, either in the master force field parameter file or the keyfile, then Tinker requires that special DIPOLE4 parameters be given for all bond dipoles in 4-membered rings. In the absence of any DIPOLE4 keywords, standard DIPOLE parameters will be used for bonds in 4-membered rings.

.. index:: DIPOLE5
.. _KEY-DIPOLE5:

DIPOLE5 [2 integers & 2 reals]
   Provides the values for a single bond dipole electrostatic parameter specific to atoms in 5-membered rings. The integer modifiers give the atom type numbers for the two kinds of atoms involved in the bond dipole which is to be defined. The real number modifiers give the value of the bond dipole in Debyes and the position of the dipole site along the bond. The default for the dipole position in the absence of a specified value is 0.5, placing the dipole at the midpoint of the bond. If any DIPOLE5 keywords are present, either in the master force field parameter file or the keyfile, then Tinker requires that special DIPOLE5 parameters be given for all bond dipoles in 5-membered rings. In the absence of any DIPOLE5 keywords, standard DIPOLE parameters will be used for bonds in 5-membered rings.

.. index:: DIPOLETERM
.. _KEY-DIPOLETERM:

DIPOLETERM [NONE/ONLY]
   Controls use of the dipole-dipole potential energy term between pairs of bond dipoles. In the absence of a modifying option, this keyword turns on use of the potential. The NONE option turns off use of this potential energy term. The ONLY option turns off all potential energy terms except for this one.

.. index:: DIRECT-11-SCALE
.. _KEY-DIRECT-11-SCALE:

DIRECT-11-SCALE [real]
   Provides a multiplicative scale factor that is applied to the permanent (direct) field due to atoms within a polarization group during an induced dipole calculation, i.e., atoms that are in the same polarization group as the atom being polarized. The default value of 0.0 is used, if the DIRECT-11-SCALE keyword is not given in either the parameter file or the keyfile.

.. index:: DIRECT-12-SCALE
.. _KEY-DIRECT-12-SCALE:

DIRECT-12-SCALE [real]
   Provides a multiplicative scale factor that is applied to the permanent (direct) field due to atoms in 1-2 polarization groups during an induced dipole calculation, i.e., atoms that are in polarization groups directly connected to the group containing the atom being polarized. The default value of 0.0 is used, if the DIRECT-12-SCALE keyword is not given in either the parameter file or the keyfile.

.. index:: DIRECT-13-SCALE
.. _KEY-DIRECT-13-SCALE:

DIRECT-13-SCALE [real]
   Provides a multiplicative scale factor that is applied to the permanent (direct) field due to atoms in 1-3 polarization groups during an induced dipole calculation, i.e., atoms that are in polarization groups separated by one group from the group containing the atom being polarized. The default value of 0.0 is used, if the DIRECT-13-SCALE keyword is not given in either the parameter file or the keyfile.

.. index:: DIRECT-14-SCALE
.. _KEY-DIRECT-14-SCALE:

DIRECT-14-SCALE [real]
   Provides a multiplicative scale factor that is applied to the permanent (direct) field due to atoms in 1-4 polarization groups during an induced dipole calculation, i.e., atoms that are in polarization groups separated by two groups from the group containing the atom being polarized. The default value of 1.0 is used, if the DIRECT-14-SCALE keyword is not given in either the parameter file or the keyfile.

.. index:: DISP-12-SCALE
.. _KEY-DISP-12-SCALE:

DISP-12-SCALE [real]
   Provides a multiplicative scale factor that is applied to dispersion potential interactions between 1-2 connected atoms, i.e., atoms that are directly bonded. The default value of 0.0 is used, if the DISP-12-SCALE keyword is not given in either the parameter file or the keyfile.

.. index:: DISP-13-SCALE
.. _KEY-DISP-13-SCALE:

DISP-13-SCALE [real]
   Provides a multiplicative scale factor that is applied to dispersion potential interactions between 1-3 connected atoms, i.e., atoms separated by two covalent bonds. The default value of 0.0 is used, if the DISP-13-SCALE keyword is not given in either the parameter file or the keyfile.

.. index:: DISP-14-SCALE
.. _KEY-DISP-14-SCALE:

DISP-14-SCALE [real]
   Provides a multiplicative scale factor that is applied to dispersion potential interactions between 1-4 connected atoms, i.e., atoms separated by three covalent bonds. The default value of 1.0 is used, if the DISP-14-SCALE keyword is not given in either the parameter file or the keyfile.

.. index:: DISP-15-SCALE
.. _KEY-DISP-15-SCALE:

DISP-15-SCALE [real]
   Provides a multiplicative scale factor that is applied to dispersion potential interactions between 1-5 connected atoms, i.e., atoms separated by four covalent bonds. The default value of 1.0 is used, if the DISP-15-SCALE keyword is not given in either the parameter file or the keyfile.

.. index:: DISP-CORRECTION
.. _KEY-DISP-CORRECTION:

DISP-CORRECTION
   Turns on the use of an isotropic long-range correction term to approximately account for dispersion interactions beyond the cutoff distance. This correction modifies the value of the dispersion energy and virial due to dispersion interactions, but has no effect on the gradient of the dispersion energy.

.. index:: DISP-CUTOFF
.. _KEY-DISP-CUTOFF:

DISP-CUTOFF [real]
   Sets the cutoff distance value in Angstroms for dispersion potential energy interactions. The energy for any pair of sites beyond the cutoff distance will be set to zero. Other keywords can be used to select a smoothing scheme near the cutoff distance. The default cutoff distance in the absence of the DISP-CUTOFF keyword is infinite for nonperiodic systems and 9.0 for periodic systems.

.. index:: DISP-LIST
.. _KEY-DISP-LIST:

DISP-LIST
   Turns on the use of pairwise neighbor lists for dispersion interactions. This method will yield identical energetic results to the standard double loop method.

.. index:: DISP-TAPER
.. _KEY-DISP-TAPER:

DISP-TAPER [real]
   Modifies the cutoff window for dispersion potential energy interactions. It is similar in form and action to the TAPER keyword, except that its value applies only to the dispersion potential. The default value in the absence of the DISP-TAPER keyword is to begin the cutoff window at 0.9 of the corresponding cutoff distance.

.. index:: DISPERSION
.. _KEY-DISPERSION:

DISPERSION [1 integer, 2 reals]
   Provides values for a single dispersion parameter. The integer modifier, if positive, gives the atom class number for which the dispersion parameters are to be defined. If the integer modifier is negative, then the parameter values to follow apply only to the individual atom whose atom number is the negative of the modifier. The real number modifiers give the root sixth-power "C6" coefficient for the atom class and the "alpha" exponent used in damping the dispersion interaction.

.. index:: DISPERSIONTERM
.. _KEY-DISPERSIONTERM:

DISPERSIONTERM [NONE/ONLY]
   Controls use of the pairwise dispersion potential energy term between pairs of atoms. In the absence of a modifying option, this keyword turns on use of the potential. The NONE option turns off use of this potential energy term. The ONLY option turns off all potential energy terms except for this one.

.. index:: DIVERGE
.. _KEY-DIVERGE:

DIVERGE [real]
   Used by the SADDLE program to set the maximum allowed value of the ratio of the gradient length along the path to the total gradient norm at the end of a cycle of minimization perpendicular to the path. If the value provided by the DIVERGE keyword is exceeded, then another cycle of maximization along the path is required. A default value of 0.005 is used in the absence of the DIVERGE keyword.

.. index:: DODECAHEDRON
.. _KEY-DODECAHEDRON:

DODECAHEDRON
   Specifies that the periodic "box" is a rhombic dodecahedron with maximal distance between parallel faces across the periodic box as given by the A-AXIS keyword. The box is oriented such that the b-axis is set equal to the a-axis, and the c-axis is longer by a factor of the square root of 2. The volume of the resulting rhombic dodecahedron is half the volume of the corresponding rectangular prism. All other unit cell and size-defining keywords are ignored if the DODECAHEDRON keyword is present.

.. index:: DPME-GRID
.. _KEY-DPME-GRID:

DPME-GRID [3 integers]
   Sets the dimensions of the reciprocal space grid used during particle mesh Ewald summation for dispersion. The three modifiers give the size along the X-, Y- and Z-axes, respectively. If either the Y- or Z-axis dimensions are omitted, then they are set equal to the X-axis dimension. The default in the absence of the PME-GRID keyword is to set the grid size along each axis to the smallest power of 2, 3 and/or 5 which is at least as large as 0.8 times the axis length in Angstoms.

.. index:: DPME-ORDER
.. _KEY-DPME-ORDER:

DPME-ORDER [integer]
   Sets the order of the B-spline interpolation used during particle mesh Ewald summation for dispersion. A default value of 4 is used in the absence of the DPME-ORDER keyword.

.. index:: ECHO
.. _KEY-ECHO:

ECHO [text string]
   Causes whatever text follows it on the keyword line to be copied directly to the output file. This keyword is also active in parameter files. It has no default value; if no text follows the ECHO keyword, a blank line is placed in the output file.

.. index:: ELE-LAMBDA
.. _KEY-ELE-LAMBDA:

ELE-LAMBDA
   Sets the value of the lambda scaling parameters for electrostatic interactions during free energy calculations and similar. The real number modifier sets the position along path from the initial state (lambda=0) to the final state (lambda=1). Alternatively, this parameter can set the state of decoupling or annihilation for specified groups from none (lambda=1) to complete (lambda=0). The groups involved in the scaling are given separately via LIGAND or MUTATE keywords.

.. index:: ELECTNEG
.. _KEY-ELECTNEG:

ELECTNEG [3 integers & 1 real]
   Provides the values for a single electronegativity bond length correction parameter. The first two integer modifiers give the atom class numbers of the atoms involved in the bond to be corrected. The third integer modifier is the atom class of an electronegative atom. In the case of a primary correction, an atom of this third class must be directly bonded to an atom of the second atom class. For a secondary correction, the third class is one atom removed from an atom of the second class. The real number modifier is the value in Angstroms by which the original ideal bond length is to be corrected.

.. index:: ELECTRIC
.. _KEY-ELECTRIC:

ELECTRIC [real]
   Specifies a value for the so-called "electric constant" allowing conversion unit of electrostatic potential energy values from electrons^2/Angstrom to kcal/mol. Internally, Tinker stores a default value for this constant as 332.063713 based on CODATA reference values. Since different force fields are intended for use with slightly different values, this keyword allows overriding the default value.

.. index:: ENFORCE-CHIRALITY
.. _KEY-ENFORCE-CHIRALITY:

ENFORCE-CHIRALITY
   Causes the chirality found at chiral tetravalent centers in the input structure to be maintained during Tinker calculations. The test for chirality is not exhaustive; two identical monovalent atoms connected to a center cause it to be marked as non-chiral, but large equivalent substituents are not detected. Trivalent "chiral" centers, for example the alpha carbon in united-atom protein structures, are not enforced as chiral.

.. index:: EPSILONRULE
.. _KEY-EPSILONRULE:

EPSILONRULE [GEOMETRIC/ARITHMETIC/HARMONIC/HHG]
   Selects the combining rule used to derive the ? value for van der Waals interactions. The default in the absence of the EPSILONRULE keyword is to use the GEOMETRIC mean of the individual epsilon values of the two atoms involved in the van der Waals interaction.

.. index:: EWALD
.. _KEY-EWALD:

EWALD
   Turns on the use of smooth particle mesh Ewald (PME) summation during computation of partial charge, atomic multipole and polarization interactions in periodic systems. By default, in the absence of the EWALD keyword, distance-based cutoffs are used for electrostatic interactions.

.. index:: EWALD-ALPHA
.. _KEY-EWALD-ALPHA:

EWALD-ALPHA [real]
   Sets the value of the Ewald coefficient which controls the width of the Gaussian screening charges during particle mesh Ewald summation for multipole electrostatics, and by default for other PME interactions. In the absence of the EWALD-ALPHA keyword, a value is chosen which causes interactions outside the real-space cutoff to be below a fixed tolerance. For most standard applications of Ewald summation, the program default should be used.

.. index:: EWALD-BOUNDARY
.. _KEY-EWALD-BOUNDARY:

EWALD-BOUNDARY
   Invokes the use of insulating (ie, vacuum) boundary conditions during Ewald summation, corresponding to the media surrounding the system having a dielectric value of 1. The default in the absence of the EWALD-BOUNDARY keyword is to use conducting (ie, tinfoil) boundary conditions where the surrounding media is assumed to have an infinite dielectric value.

.. index:: EWALD-CUTOFF
.. _KEY-EWALD-CUTOFF:

EWALD-CUTOFF [real]
   Sets the value in Angstroms of the real-space distance cutoff for use during Ewald summation. By default, in the absence of the EWALD-CUTOFF keyword, a value of 7.0 is used.

.. index:: EXIT-PAUSE
.. _KEY-EXIT-PAUSE:

EXIT-PAUSE
   Causes Tinker programs to pause and wait for a carriage return at the end of executation prior to returning control to the operating system. This is useful to keep the execution window open following termination on machines running Microsoft Windows or Apple macOS. The default in the absence of the EXIT-PAUSE keyword, is to return control to the operating system immediately at program termination.

.. index:: EXTRATERM
.. _KEY-EXTRATERM:

EXTRATERM [NONE/ONLY]
   Controls use of the user defined extra potential energy term. In the absence of a modifying option, this keyword turns on use of the potential. The NONE option turns off use of this potential energy term. The ONLY option turns off all potential energy terms except for this one.

.. index:: FCTMIN
.. _KEY-FCTMIN:

FCTMIN [real]
   Sets a convergence criterion for successful completion of an optimization. If the value of the optimization objective function, typically the potential energy, falls below the value set by FCTMIN, then the optimization is deemed to have converged. The default value in the absence of the FCTMIN keyword is -1000000, effectively removing this criterion as a possible agent for termination.

.. index:: FFT-PACKAGE
.. _KEY-FFT-PACKAGE:

FFT-PACKAGE [FFTPACK/FFTW]
   Specifies the fast Fourier transform package to be used in reciprocal space calculations as part of particle mesh Ewald summation. The default in the absence of the FFT-PACKAGE keyword is to use FFTPACK for serial, single-threaded calculations, and FFTW for OpenMP parallel calculations using multiple threads.

FIT-ANGLE

FIT-BOND

FIT-OPBEND

FIT-STRBND

FIT-TORSION

FIT-UREY

FIX-ANGLE

FIX-BOND

FIX-DIPOLE

FIX-MONOPOLE

FIX-OPBEND

FIX-QUADRUPOLE

FIX-STRBND

FIX-TORSION

FIX-UREY

.. index:: FORCEFIELD
.. _KEY-FORCEFIELD:

FORCEFIELD [name]
   Provides a name for the force field to be used in the current calculation. Its value is usually set in the master force field parameter file for the calculation (see the PARAMETERS keyword) instead of in the keyfile.

.. index:: FRICTION
.. _KEY-FRICTION:

FRICTION [real]
   Sets the value of the frictional coefficient in 1/ps for use with stochastic dynamics. The default value used in the absence of the FRICTION keyword is 91.0, which is generally appropriate for water.

.. index:: FRICTION-SCALING
.. _KEY-FRICTION-SCALING:

FRICTION-SCALING
   Turns on the use of atomic surface area-based scaling of the frictional coefficient during stochastic dynamics. When in use, the coefficient for each atom is multiplied by that atom's fraction of exposed surface area. The default in the absence of the keyword is to omit the scaling and use the full coefficient value for each atom.

.. index:: GAMMA
.. _KEY-GAMMA:

GAMMA [real]
   Sets the value of the gamma angle of a crystal unit cell, i.e., the angle between the a-axis and b-axis of a unit cell, or, equivalently, the angle between the X-axis and Y-axis of a periodic box. The default value in the absence of the GAMMA keyword is to set the gamma angle equal to the gamma angle as given by the keyword ALPHA.

.. index:: GAMMA-HALGREN
.. _KEY-GAMMA-HALGREN:

GAMMA-HALGREN [real]
   Sets the value of the gamma parameter in Halgren's buffered 14-7 vdw potential energy functional form. In the absence of the GAMMA-HALGREN keyword, a default value of 0.12 is used.

.. index:: GAMMAMIN
.. _KEY-GAMMAMIN:

GAMMAMIN [real]
   Sets the convergence target value for gamma during searches for maxima along the quadratic synchronous transit used by the SADDLE program. The value of gamma is the square of the ratio of the gradient projection along the path to the total gradient. A default value of 0.00001 is used in the absence of the GAMMAMIN keyword.

.. index:: GAUSSTYPE
.. _KEY-GAUSSTYPE:

GAUSSTYPE [LJ-2/LJ-4/MM2-2/MM3-2/IN-PLACE]
   Specifies the underlying vdw form that a Gaussian vdw approximation will attempt to fit as the number of terms to be used in a Gaussian approximation of the Lennard-Jones van der Waals potential. The text modifier gives the name of the functional form to be used. Thus LJ-2 as a modifier will result in a 2-Gaussian fit to a Lennard-Jones vdw potential. The GAUSSTYPE keyword only takes effect when VDWTYPE is set to GAUSSIAN. This keyword has no default value.

GK-RADIUS

GKC

GKR

.. index:: GROUP
.. _KEY-GROUP:

GROUP [integer, integer list]
   Defines an atom group as a substructure within the full input molecular structure. The value of the first integer is the group number which must be in the range from 1 to the maximum number of allowed groups. The remaining intergers give the atom or atoms contained in this group as one or more atom numbers or ranges. Multiple keyword lines can be used to specify additional atoms in the same group. Note that an atom can only be in one group, the last group to which it is assigned is the one used.

.. index:: GROUP-INTER
.. _KEY-GROUP-INTER:

GROUP-INTER
   Assigns a value of 1.0 to all inter-group interactions and a value of 0.0 to all intra-group interactions. For example, combination with the GROUP-MOLECULE keyword provides for rigid-body calculations.

.. index:: GROUP-INTRA
.. _KEY-GROUP-INTRA:

GROUP-INTRA
   Assigns a value of 1.0 to all intra-group interactions and a value of 0.0 to all inter-group interactions.

.. index:: GROUP-MOLECULE
.. _KEY-GROUP-MOLECULE:

GROUP-MOLECULE
   Sets each individual molecule in the system to be a separate atom group, but does not assign weights to group-group interactions.

.. index:: GROUP-SELECT
.. _KEY-GROUP-SELECT:

GROUP-SELECT [2 integers, real]
   Assigns a weight in the final potential energy of a specified set of intra- or intergroup interactions. The integer modifiers give the group numbers of the groups involved. If the two numbers are the same, then an intragroup set of interactions is specified. The real modifier gives the weight by which all energetic interactions in this set will be multiplied before incorporation into the final potential energy. If omitted as a keyword modifier, the weight will be set to 1.0 by default. If any SELECT-GROUP keywords are present, then any set of interactions not specified in a SELECT-GROUP keyword is given a zero weight. The default when no SELECT-GROUP keywords are specified is to use all intergroup interactions with a weight of 1.0 and to set all intragroup interactions to zero.

.. index:: HBOND
.. _KEY-HBOND:

HBOND [2 integers & 2 reals]
   Provides the values for the MM3-style directional hydrogen bonding parameters for a single pair of atoms. The integer modifiers give the pair of atom class numbers for which hydrogen bonding parameters are to be defined. The two real number modifiers give the values of the minimum energy contact distance in Angstroms and the well depth at the minimum distance in kcal/mole.

.. index:: HEAVY-HYDROGEN
.. _KEY-HEAVY-HYDROGEN:

HEAVY-HYDROGEN [real]
   Turns on use of hydrogen mass repartitioning (HMR) and sets the target value for hydrogen masses. HMR transfers atomic mass from heavy atoms to their attached hydrogen atoms. Mass transfer is allowed until the hydrogen mass target is reached, or until a heavy atom and its attached hydrogens all have equal mass. A default value of 4.0 is used as the hydrogen mass target in the absence of the HEAVY-HYDROGEN keyword.

.. index:: HESSIAN-CUTOFF
.. _KEY-HESSIAN-CUTOFF:

HESSIAN-CUTOFF [real]
   Defines a lower limit for significant Hessian matrix elements. During computation of the Hessian matrix of partial second derivatives, any matrix elements with absolute value below HESS-CUTOFF will be set to zero and omitted from the sparse matrix Hessian storage scheme used by Tinker. For most calculations, the default in the absence of this keyword is zero, i.e., all elements will be stored. For most truncated Newton optimizations the Hessian cutoff will be chosen dynamically by the optimizer.

.. index:: HGUESS
.. _KEY-HGUESS:

HGUESS [real]
   Sets an initial guess for the average value of the diagonal elements of the scaled inverse Hessian matrix used by the optimally conditioned variable metric optimization routine. A default value of 0.4 is used in the absence of the HGUESS keyword.

IEL-SCF

.. index:: IMPROPER
.. _KEY-IMPROPER:

IMPROPER [4 integers & 2 reals]
   Provides the values for a single CHARMM-style improper dihedral angle parameter. The integer modifiers give the atom class numbers for the four kinds of atoms involved in the torsion which is to be defined. The real number modifiers give the force constant value for the deviation from the target improper torsional angle, and the target value for the torsional angle, respectively. The default units for the improper force constant are kcal/mole/radian^2, but this can be controlled via the IMPROPUNIT keyword.

.. index:: IMPROPTERM
.. _KEY-IMPROPTERM:

IMPROPTERM [NONE/ONLY]
   Controls use of the CHARMM-style improper dihedral angle potential energy term. In the absence of a modifying option, this keyword turns on use of the potential. The NONE option turns off use of this potential energy term. The ONLY option turns off all potential energy terms except for this one.

.. index:: IMPROPUNIT
.. _KEY-IMPROPUNIT:

IMPROPUNIT [real]
   Sets the scale factor needed to convert the energy value computed by the CHARMM-style improper dihedral angle potential into units of kcal/mole. The correct value is force field dependent and typically provided in the header of the master force field parameter file. The default value of (180/Pi)^2 = 0.0003046 is used, if the IMPROPUNIT keyword is not given in the force field parameter file or the keyfile.

.. index:: IMPTORS
.. _KEY-IMPTORS:

IMPTORS [4 integers & up to 3 real/real/integer triples]
   Provides the values for a single AMBER-style improper torsional angle parameter. The first four integer modifiers give the atom class numbers for the atoms involved in the improper torsional angle to be defined. By convention, the third atom class of the four is the trigonal atom on which the improper torsion is centered. The torsional angle computed is literally that defined by the four atom classes in the order specified by the keyword. Each of the remaining triples of real/real/integer modifiers give the half-amplitude, phase offset in degrees and periodicity of a particular improper torsional term, respectively. Periodicities through 3-fold are allowed for improper torsional parameters.

.. index:: IMPTORSTERM
.. _KEY-IMPTORSTERM:

IMPTORSTERM [NONE/ONLY]
   Controls use of the AMBER-style improper torsional angle potential energy term. In the absence of a modifying option, this keyword turns on use of the potential. The NONE option turns off use of this potential energy term. The ONLY option turns off all potential energy terms except for this one.

.. index:: IMPTORSUNIT
.. _KEY-IMPTORSUNIT:

IMPTORSUNIT [real]
   Sets the scale factor needed to convert the energy value computed by the AMBER-style improper torsional angle potential into units of kcal/mole. The correct value is force field dependent and typically provided in the header of the master force field parameter file. The default value of 1.0 is used, if the IMPTORSUNIT keyword is not given in the force field parameter file or the keyfile.

.. index:: INACTIVE
.. _KEY-INACTIVE:

INACTIVE [integer list]
   Sets the list of inactive atoms during a Tinker computation. Individual potential energy terms are not computed when all atoms involved in the term are inactive. For Cartesian space calculations, inactive atoms are not allowed to move. For torsional space calculations, rotations are not allowed when there are inactive atoms on both sides of the rotated bond. Multiple INACTIVE lines can be present in the keyfile, and on each line the keyword can be followed by one or more atom numbers or ranges. If any INACTIVE keys are found, all atoms are set to active except those listed on the INACTIVE lines. The ACTIVE keyword overrides all INACTIVE keywords found in the keyfile.

INDUCE-12-SCALE

INDUCE-13-SCALE

INDUCE-14-SCALE

INDUCE-15-SCALE

.. index:: INTEGRATOR
.. _KEY-INTEGRATOR:

INTEGRATOR [VERLET/BEEMAN/STOCHASTIC/RIGIDBODY]
   Chooses the integration method for propagation of dynamics trajectories. The keyword is followed on the same line by the name of the option. Standard Newtonian MD can be run using either VERLET for the Velocity Verlet method, or BEEMAN for the velocity form of Bernie Brook's "Better Beeman" method. A Velocity Verlet-based stochastic dynamics trajectory is selected by the STOCHASTIC modifier. A rigid-body dynamics method is selected by the RIGIDBODY modifier. The default integration scheme is MD using the BEEMAN method.

.. index:: INTMAX
.. _KEY-INTMAX:

INTMAX [integer]
   Sets the maximum number of interpolation cycles that will be allowed during the line search phase of an optimization. All gradient-based Tinker optimization routines use a common line search routine involving quadratic extrapolation and cubic interpolation. If the value of INTMAX is reached, an error status is set for the line search and the search is repeated with a much smaller initial step size. The default value in the absence of this keyword is optimization routine dependent, but is usually in the range 5 to 10.

.. index:: LAMBDA
.. _KEY-LAMBDA:

LAMBDA [real]
   Sets the value of the lambda scaling parameters for electrostatic, vdw and torsional interactions during free energy calculations and similar. The real number modifier sets the position along path from the initial state (lambda=0) to the final state (lambda=1). Alternatively, this parameter can set the state of decoupling or annihilation for specified groups from none (lambda=1) to complete (lambda=0). The groups involved in the scaling are given separately via LIGAND or MUTATE keywords.

.. index:: LBFGS-VECTORS
.. _KEY-LBFGS-VECTORS:

LBFGS-VECTORS [integer]
   Sets the number of correction vectors used by the limited-memory L-BFGS optimization routine. The current maximum allowable value, and the default in the absence of the LBFGS-VECTORS keyword is 15.

LIGAND

.. index:: LIGHTS
.. _KEY-LIGHTS:

LIGHTS
   Turns on Method of Lights neighbor generation for the partial charge electrostatics and any of the van der Waals potentials. This method will yield identical energetic results to the standard double loop method. Method of Lights will be faster when the volume of a sphere with radius equal to the nonbond cutoff distance is significantly less than half the volume of the total system (i.e., the full molecular system, the crystal unit cell or the periodic box). It requires less storage than pairwise neighbor lists.

.. index:: LIST-BUFFER
.. _KEY-LIST-BUFFER:

LIST-BUFFER [real]
   Sets the size of the neighbor list buffer in Angstroms for potential energy functions. This value is added to the actual cutoff distance to determine which pairs will be kept on the neighbor list. This buffer value is used for all potential function neighbor lists. The default value in the absence of the LIST-BUFFER keyword is 2.0 Angstroms.

.. index:: MAXITER
.. _KEY-MAXITER:

MAXITER [integer]
   Sets the maximum number of minimization iterations that will be allowed for any Tinker program that uses any of the nonlinear optimization routines. The default value in the absence of this keyword is program dependent, but is always set to a very large number.

.. index:: METAL
.. _KEY-METAL:

METAL [integer]
   Provides the values for a single transition metal ligand field parameter. Note the current version just reads an atom class number and does not set any parameters. This keyword is present in the code, but not active in the current version of Tinker.

.. index:: METALTERM
.. _KEY-METALTERM:

METALTERM [NONE/ONLY]
   Controls use of the transition metal ligand field potential energy term. In the absence of a modifying option, this keyword turns on use of the potential. The NONE option turns off use of this potential energy term. The ONLY option turns off all potential energy terms except for this one.

MMFF-PIBOND

MMFFANGLE

MMFFAROM

MMFFBCI

MMFFBOND

MMFFBONDER

MMFFCOVRAD

MMFFDEFSTBN

MMFFEQUIV

MMFFOPBEND

MMFFPBCI

MMFFPROP

MMFFSTRBND

MMFFTORSION

MMFFVDW

.. index:: MPOLE-12-SCALE
.. _KEY-MPOLE-12-SCALE:

MPOLE-12-SCALE [real]
   Provides a multiplicative scale factor that is applied to permanent atomic multipole electrostatic interactions between 1-2 connected atoms, i.e., atoms that are directly bonded. The default value of 0.0 is used, if the MPOLE-12-SCALE keyword is not given in either the parameter file or the keyfile.

.. index:: MPOLE-13-SCALE
.. _KEY-MPOLE-13-SCALE:

MPOLE-13-SCALE [real]
   Provides a multiplicative scale factor that is applied to permanent atomic multipole  electrostatic interactions between 1-3 connected atoms, i.e., atoms separated by two covalent bonds. The default value of 0.0 is used, if the MPOLE-13-SCALE keyword is not given in either the parameter file or the keyfile.

.. index:: MPOLE-14-SCALE
.. _KEY-MPOLE-14-SCALE:

MPOLE-14-SCALE [real]
   Provides a multiplicative scale factor that is applied to permanent atomic multipole  electrostatic interactions between 1-4 connected atoms, i.e., atoms separated by three covalent bonds. The default value of 1.0 is used, if the MPOLE-14-SCALE keyword is not given in either the parameter file or the keyfile.

.. index:: MPOLE-15-SCALE
.. _KEY-MPOLE-15-SCALE:

MPOLE-15-SCALE [real]
   Provides a multiplicative scale factor that is applied to permanent atomic multipole  electrostatic interactions between 1-5 connected atoms, i.e., atoms separated by four covalent bonds. The default value of 1.0 is used, if the MPOLE-15-SCALE keyword is not given in either the parameter file or the keyfile.

.. index:: MPOLE-CUTOFF
.. _KEY-MPOLE-CUTOFF:

MPOLE-CUTOFF [real]
   Sets the cutoff distance value in Angstroms for atomic multipole potential energy interactions. The energy for any pair of sites beyond the cutoff distance will be set to zero. Other keywords can be used to select a smoothing scheme near the cutoff distance. The default cutoff distance in the absence of the MPOLE-CUTOFF keyword is infinite for nonperiodic systems and 9.0 for periodic systems.

.. index:: MPOLE-LIST
.. _KEY-MPOLE-LIST:

MPOLE-LIST
   Turns on pairwise neighbor lists for atomic multipole electrostatics and induced dipole polarization. This method will yield identical energetic results to the standard double loop methods.

.. index:: MPOLE-TAPER
.. _KEY-MPOLE-TAPER:

MPOLE-TAPER [real]
   Modifies the cutoff window for atomic multipole potential energy interactions. It is similar in form and action to the TAPER keyword, except that its value applies only to the atomic multipole potential. The default value in the absence of the MPOLE-TAPER keyword is to begin the cutoff window at 0.65 of the corresponding cutoff distance.

.. index:: MULTIPOLE
.. _KEY-MULTIPOLE:

MULTIPOLE [5 lines with: 3 or 4 integers & 1 real; 3 reals; 1 real; 2 reals; 3 reals]
   Provides the values for a set of atomic multipole parameters at a single site. A complete keyword entry consists of three consequtive lines, the first line containing the MULTIPOLE keyword and the two following lines. The first line contains three integers which define the atom type on which the multipoles are centered, and the Z-axis and X-axis defining atom types for this center. The optional fourth integer contains the Y-axis defining atom type, and is only required for locally chiral multipole sites. The real number on the first line gives the monopole (atomic charge) in electrons. The second line contains three real numbers which give the X-, Y- and Z-components of the atomic dipole in electron-Ang. The final three lines, consisting of one, two and three real numbers give the upper triangle of the traceless atomic quadrupole tensor in electron-Ang^2.

.. index:: MULTIPOLETERM
.. _KEY-MULTIPOLETERM:

MULTIPOLETERM [NONE/ONLY]
   Controls use of the atomic multipole electrostatics potential energy term. In the absence of a modifying option, this keyword turns on use of the potential. The NONE option turns off use of this potential energy term. The ONLY option turns off all potential energy terms except for this one.

.. index:: MUTATE
.. _KEY-MUTATE:

MUTATE [3 integers]
   Specifies atoms to be mutated during free energy perturbation calculations. The first integer modifier gives the atom number of an atom in the current system. The final two modifier values give the atom types corresponding the the lambda=0 and lambda=1 states of the specified atom.

.. index:: MUTUAL-11-SCALE
.. _KEY-MUTUAL-11-SCALE:

MUTUAL-11-SCALE [real]
   Provides a multiplicative scale factor that is applied to the induced (mutual) field due to atoms within a polarization group during an induced dipole calculation, i.e., atoms that are in the same polarization group as the atom being polarized. The default value of 1.0 is used, if the MUTUAL-11-SCALE keyword is not given in either the parameter file or the keyfile.

.. index:: MUTUAL-12-SCALE
.. _KEY-MUTUAL-12-SCALE:

MUTUAL-12-SCALE [real]
   Provides a multiplicative scale factor that is applied to the induced (mutual) field due to atoms in 1-2 polarization groups during an induced dipole calculation, i.e., atoms that are in polarization groups directly connected to the group containing the atom being polarized. The default value of 1.0 is used, if the MUTUAL-12-SCALE keyword is not given in either the parameter file or the keyfile.

.. index:: MUTUAL-13-SCALE
.. _KEY-MUTUAL-13-SCALE:

MUTUAL-13-SCALE [real]
   Provides a multiplicative scale factor that is applied to the induced (mutual) field due to atoms in 1-3 polarization groups during an induced dipole calculation, i.e., atoms that are in polarization groups separated by one group from the group containing the atom being polarized. The default value of 1.0 is used, if the MUTUAL-13-SCALE keyword is not given in either the parameter file or the keyfile.

.. index:: MUTUAL-14-SCALE
.. _KEY-MUTUAL-14-SCALE:

MUTUAL-14-SCALE [real]
   Provides a multiplicative scale factor that is applied to the induced (mutual) field due to atoms in 1-4 polarization groups during an induced dipole calculation, i.e., atoms that are in polarization groups separated by two groups from the group containing the atom being polarized. The default value of 1.0 is used, if the MUTUAL-14-SCALE keyword is not given in either the parameter file or the keyfile.

.. index:: NEIGHBOR-GROUPS
.. _KEY-NEIGHBOR-GROUPS:

NEIGHBOR-GROUPS
   Causes the attached atom to be used in determining the charge-charge neighbor distance for all monovalent atoms in the molecular system. Its use causes all monovalent atoms to be treated the same as their attached atoms for purposes of including or scaling 1-2, 1-3 and 1-4 interactions. This option works only for the simple charge-charge electrostatic potential; it does not affect bond dipole or atomic multipole potentials. The NEIGHBOR-GROUPS scheme is similar to that used by ENCAD and other force fields.

.. index:: NEIGHBOR-LIST
.. _KEY-NEIGHBOR-LIST:

NEIGHBOR-LIST
   Turns on pairwise neighbor lists for partial charge electrostatics, atomic multipole electrostatics, induced dipole polarization and any of the van der Waals potentials. This method will yield identical energetic results to the standard double loop method.

.. index:: NEUTRAL-GROUPS
.. _KEY-NEUTRAL-GROUPS:

NEUTRAL-GROUPS
   Causes the attached atom to be used in determining the charge-charge interaction cutoff distance for all monovalent atoms in the molecular system. Its use reduces cutoff discontinuities by avoiding splitting many of the largest charge separations found in typical molecules. Note that this keyword does not rigorously implement the usual concept of a "neutral group" as used in the literature with some versions of OPLS and other force fields. This option works only for the simple charge-charge electrostatic potential; it does not affect bond dipole or atomic multipole potentials.

.. index:: NEWHESS
.. _KEY-NEWHESS:

NEWHESS [integer]
   Sets the number of algorithmic iterations between recomputation of the Hessian matrix. At present this keyword applies exclusively to optimizations using the truncated Newton method. The default value in the absence of this keyword is 1, i.e., the Hessian is computed on every iteration.

.. index:: NEXTITER
.. _KEY-NEXTITER:

NEXTITER [integer]
   Sets the iteration number to be used for the first iteration of the current computation. At present this keyword applies to optimization procedures where its use can effect convergence criteria, timing of restarts, and so forth. The default in the absence of this keyword is to take the initial iteration as iteration 1.

.. index:: NOARCHIVE
.. _KEY-NOARCHIVE:

NOARCHIVE
   Causes Tinker molecular dynamics-based programs to write trajectories directly to "cycle" files with a sequentially numbered file extension. The default, in the absence of this keyword, is to write a single plain-text archive file with the .arc format. If an archive file already exists at the start of the calculation, then the newly generated trajectory is appended to the end of the existing file. The default in the absence of this keyword is to write the trajectory snapshots to consecutively numbered cycle files.

.. index:: NOSYMMETRY
.. _KEY-NOSYMMETRY:

NOSYMMETRY
   Forces the use of triclinic periodic boundary conditions and minimum image generation regardless of any symmetry or equilvalent values in the periodic box or crystal lattice values. Used to allow the possibility of symmetry breaking during calculations that begin from a symmetric structure.

.. index:: NOVERSION
.. _KEY-NOVERSION:

NOVERSION
   Turns off the use of version numbers appended to the end of filenames as the method for generating filenames for updated copies of an existing file. The presence of this keyword results in direct use of input file names without a search for the highest available version, and requires the entry of specific output file names in many additional cases. By default, in the absence of this keyword, Tinker generates and attaches version numbers in a manner similar to the Digital OpenVMS operating system. For example, subsequent new versions of the file molecule.xyz would be written first to the file molecule.xyz_2, then to molecule.xyz_3, etc.

.. index:: OCTAHEDRON
.. _KEY-OCTAHEDRON:

OCTAHEDRON
   Specifies that the periodic "box" is a truncated octahedron with maximal distance between parallel faces across the periodic box as given by the A-AXIS keyword. The b-axis and c-axis are set equal to the a-axis, the volume of the resulting truncated octahedron is half the volume of the corresponding rectangular prism. All other unit cell and size-defining keywords are ignored if the OCTAHEDRON keyword is present.

.. index:: OPBEND
.. _KEY-OPBEND:

OPBEND [4 integers & 1 real]
   Provides the values for a single out-of-plane bending potential parameter. The first integer modifier is the atom class of the out-of-plane atom and the second integer is the atom class of the central trigonal atom. The third and fourth integers give the atom classes of the two remaining atoms attached to the trigonal atom. Values of zero for the third and fourth integers are treated as wildcards, and can represent any atom type. The real number modifier gives the force constant value for the out-of-plane angle. The default units for the force constant are kcal/mole/radian^2, but this can be controlled via the OPBENDUNIT keyword.

.. index:: OPBEND-CUBIC
.. _KEY-OPBEND-CUBIC:

OPBEND-CUBIC [real]
   Sets the value of the cubic term in the Taylor series expansion form of the out-of-plane bending potential energy. The real number modifier gives the value of the coefficient as a multiple of the quadratic coefficient. This term multiplied by the out-of-plane bending energy unit conversion factor, the force constant, and the cube of the deviation of the out-of-plane angle from zero gives the cubic contribution to the out-of-plane bending energy. The default value in the absence of the OPBEND-CUBIC keyword is zero; i.e., the cubic out-of-plane bending term is omitted.

.. index:: OPBEND-PENTIC
.. _KEY-OPBEND-PENTIC:

OPBEND-PENTIC [real]
   Sets the value of the fifth power term in the Taylor series expansion form of the out-of-plane bending potential energy. The real number modifier gives the value of the coefficient as a multiple of the quadratic coefficient. This term multiplied by the out-of-plane bending energy unit conversion factor, the force constant, and the fifth power of the deviation of the out-of-plane angle from zero gives the pentic contribution to the out-of-plane bending energy. The default value in the absence of the OPBEND-PENTIC keyword is zero; i.e., the pentic out-of-plane bending term is omitted.

.. index:: OPBEND-QUARTIC
.. _KEY-OPBEND-QUARTIC:

OPBEND-QUARTIC [real]
   Sets the value of the quartic term in the Taylor series expansion form of the out-of-plane bending potential energy. The real number modifier gives the value of the coefficient as a multiple of the quadratic coefficient. This term multiplied by the out-of-plane bending energy unit conversion factor, the force constant, and the forth power of the deviation of the out-of-plane angle from zero gives the quartic contribution to the out-of-plane bending energy. The default value in the absence of the OPBEND-QUARTIC keyword is zero; i.e., the quartic out-of-plane bending term is omitted.

.. index:: OPBEND-SEXTIC
.. _KEY-OPBEND-SEXTIC:

OPBEND-SEXTIC [real]
   Sets the value of the sixth power term in the Taylor series expansion form of the out-of-plane bending potential energy. The real number modifier gives the value of the coefficient as a multiple of the quadratic coefficient. This term multiplied by the out-of-plane bending energy unit conversion factor, the force constant, and the sixth power of the deviation of the out-of-plane angle from zero gives the sextic contribution to the out-of-plane bending energy. The default value in the absence of the OPBEND-SEXTIC keyword is zero; i.e., the sextic out-of-plane bending term is omitted.

.. index:: OPBENDTERM
.. _KEY-OPBENDTERM:

OPBENDTERM [NONE/ONLY]
   Controls use of the out-of-plane bending potential energy term. In the absence of a modifying option, this keyword turns on use of the potential. The NONE option turns off use of this potential energy term. The ONLY option turns off all potential energy terms except for this one.

.. index:: OPBENDTYPE
.. _KEY-OPBENDTYPE:

OPBENDTYPE [W-D-C/Allinger]
   Sets the type of angle to be used in the out-of-plane bending potential energy term. The choices are to use the Wilson-Decius-Cross (W-D-C) formulation from vibrational spectroscopy, or the Allinger angle from the MM2/MM3 force fields. The default value in the absence of the OPBENDTYPE keyword is to use the W-D-C angle.

.. index:: OPBENDUNIT
.. _KEY-OPBENDUNIT:

OPBENDUNIT [real]
   Sets the scale factor needed to convert the energy value computed by the out-of-plane bending potential into units of kcal/mole. The correct value is force field dependent and typically provided in the header of the master force field parameter file. The default of (Pi/180)^2 = 0.0003046 is used, if the OPBENDUNIT keyword is not given in the force field parameter file or the keyfile.

.. index:: OPDIST
.. _KEY-OPDIST:

OPDIST [4 integers & 1 real]
   Provides the values for a single out-of-plane distance potential parameter. The first integer modifier is the atom class of the central trigonal atom and the three following integer modifiers are the atom classes of the three attached atoms. The real number modifier is the force constant for the harmonic function of the out-of-plane distance of the central atom. The default units for the force constant are kcal/mole/Ang^2, but this can be controlled via the OPDISTUNIT keyword.

.. index:: OPDIST-CUBIC
.. _KEY-OPDIST-CUBIC:

OPDIST-CUBIC [real]
   Sets the value of the cubic term in the Taylor series expansion form of the out-of-plane distance potential energy. The real number modifier gives the value of the coefficient as a multiple of the quadratic coefficient. This term multiplied by the out-of-plane distance energy unit conversion factor, the force constant, and the cube of the deviation of the out-of-plane distance from zero gives the cubic contribution to the out-of-plane distance energy. The default value in the absence of the OPDIST-CUBIC keyword is zero; i.e., the cubic out-of-plane distance term is omitted.

.. index:: OPDIST-PENTIC
.. _KEY-OPDIST-PENTIC:

OPDIST-PENTIC [real]
   Sets the value of the fifth power term in the Taylor series expansion form of the out-of-plane distance potential energy. The real number modifier gives the value of the coefficient as a multiple of the quadratic coefficient. This term multiplied by the out-of-plane distance energy unit conversion factor, the force constant, and the fifth power of the deviation of the out-of-plane distance from zero gives the pentic contribution to the out-of-plane distance energy. The default value in the absence of the OPDIST-PENTIC keyword is zero; i.e., the pentic out-of-plane distance term is omitted.

.. index:: OPDIST-QUARTIC
.. _KEY-OPDIST-QUARTIC:

OPDIST-QUARTIC [real]
   Sets the value of the quartic term in the Taylor series expansion form of the out-of-plane distance potential energy. The real number modifier gives the value of the coefficient as a multiple of the quadratic coefficient. This term multiplied by the out-of-plane distance energy unit conversion factor, the force constant, and the forth power of the deviation of the out-of-plane distance from zero gives the quartic contribution to the out-of-plane distance energy. The default value in the absence of the OPDIST-QUARTIC keyword is zero; i.e., the quartic out-of-plane distance term is omitted.

.. index:: OPDIST-SEXTIC
.. _KEY-OPDIST-SEXTIC:

OPDIST-SEXTIC [real]
   Sets the value of the sixth power term in the Taylor series expansion form of the out-of-plane distance potential energy. The real number modifier gives the value of the coefficient as a multiple of the quadratic coefficient. This term multiplied by the out-of-plane distance energy unit conversion factor, the force constant, and the sixth power of the deviation of the out-of-plane distance from zero gives the sextic contribution to the out-of-plane distance energy. The default value in the absence of the OPDIST-SEXTIC keyword is zero; i.e., the sextic out-of-plane distance term is omitted.

.. index:: OPDISTTERM
.. _KEY-OPDISTTERM:

OPDISTTERM [NONE/ONLY]
   Controls use of the out-of-plane distance potential energy term. In the absence of a modifying option, this keyword turns on use of the potential. The NONE option turns off use of this potential energy term. The ONLY option turns off all potential energy terms except for this one.

.. index:: OPDISTUNIT
.. _KEY-OPDISTUNIT:

OPDISTUNIT [real]
   Sets the scale factor needed to convert the energy value computed by the out-of-plane distance potential into units of kcal/mole. The correct value is force field dependent and typically provided in the header of the master force field parameter file. The default value of 1.0 is used, if the OPDISTUNIT keyword is not given in the force field parameter file or the keyfile.

.. index:: OPENMP-THREADS
.. _KEY-OPENMP-THREADS:

OPENMP-THREADS [integer]
   Sets the number of threads to be used in OpenMP parallelization of certain Tinker calculations. The default in the absence of the OPENMP-THREADS keyword is to set the number of threads equal to the total number of CPU cores found for the computer being used.

OPT-COEFF

.. index:: OVERWRITE
.. _KEY-OVERWRITE:

OVERWRITE
   Causes Tinker programs, such as minimizations, that output intermediate coordinate sets to create a single disk file for the intermediate results which is successively overwritten with the new intermediate coordinates as they become available. This keyword is essentially the opposite of the SAVECYCLE keyword.

.. index:: PARAMETERS
.. _KEY-PARAMETERS:

PARAMETERS [file name]
   Provides the name of the force field parameter file to be used for the current Tinker calculation. The standard file name extension for parameter files, .prm, is an optional part of the file name modifier. The default in the absence of the PARAMETERS keyword is to look for a parameter file with the same base name as the molecular system and ending in the .prm extension. If a valid parameter file is not found, the user will asked to provide a file name interactively.

PCG-GUESS

PCG-NOGUESS

PCG-NOPRECOND

PCG-PEEK

PCG-PRECOND

PENETRATION

PEWALD-ALPHA [real]   Sets the value of the Ewald coefficient which controls the width of the Gaussian screening charges during particle mesh Ewald summation for polarization interactions. In the absence of the PEWALD-ALPHA keyword, the EWALD-ALPHA is used, or a value is chosen which causes interactions outside the real-space cutoff to be below a fixed tolerance. For most standard applications of polarization Ewald summation, the program default should be used.

.. index:: PIATOM
.. _KEY-PIATOM:

PIATOM [1 integer & 3 reals]
   Provides the values for the pisystem MO potential parameters for a single atom class belonging to a pisystem.

.. index:: PIBOND
.. _KEY-PIBOND:

PIBOND [2 integers & 2 reals]
   Provides the values for the pisystem MO potential parameters for a single type of pisystem bond.

.. index:: PIBOND4
.. _KEY-PIBOND4:

PIBOND4 [2 integers & 2 reals]
   Provides the values for the pisystem MO potential parameters for a single type of pisystem bond contained in a 4-membered ring.

.. index:: PIBOND5
.. _KEY-PIBOND5:

PIBOND5 [2 integers & 2 reals]
   Provides the values for the pisystem MO potential parameters for a single type of pisystem bond contained in a 5-membered ring.

.. index:: PISYSTEM
.. _KEY-PISYSTEM:

PISYSTEM [integer list]
   Sets the atoms within a molecule that are part of a conjugated pi-orbital system. The keyword is followed on the same line by a list of atom numbers and/or atom ranges that constitute the pi-system. The Allinger MM force fields use this information to set up an MO calculation used to scale bond and torsion parameters involving pi-system atoms.

.. index:: PITORS
.. _KEY-PITORS:

PITORS [2 integers & 1 real]
   Provides the values for a single pi-orbital torsional angle potential parameter. The two integer modifiers give the atom class numbers for the atoms involved in the central bond of the torsional angle to be parameterized. The real modifier gives the value of the 2-fold Fourier amplitude for the torsional angle between p-orbitals centered on the defined bond atom classes. The default units for the stretch-torsion force constant can be controlled via the PITORSUNIT keyword.

.. index:: PITORSTERM
.. _KEY-PITORSTERM:

PITORSTERM [NONE/ONLY]
   Controls use of the pi-orbital torsional angle potential energy term. In the absence of a modifying option, this keyword turns on use of the potential. The NONE option turns off use of this potential energy term. The ONLY option turns off all potential energy terms except for this one.

.. index:: PITORSUNIT
.. _KEY-PITORSUNIT:

PITORSUNIT [real]
   Sets the scale factor needed to convert the energy value computed by the pi-orbital torsional angle potential into units of kcal/mole. The correct value is force field dependent and typically provided in the header of the master force field parameter file. The default value of 1.0 is used, if the PITORSUNIT keyword is not given in the force field parameter file or the keyfile.

.. index:: PME-GRID
.. _KEY-PME-GRID:

PME-GRID [3 integers]
   Sets the dimensions of the reciprocal space grid used during particle mesh Ewald summation for electrostatics. The three modifiers give the size along the X-, Y- and Z-axes, respectively. If either the Y- or Z-axis dimensions are omitted, then they are set equal to the X-axis dimension. The default in the absence of the PME-GRID keyword is to set the grid size along each axis to the smallest power of 2, 3 and/or 5 which is at least as large as 1.2 times the axis length in Angstoms.

.. index:: PME-ORDER
.. _KEY-PME-ORDER:

PME-ORDER [integer]
   Sets the order of the B-spline interpolation used during particle mesh Ewald summation for partial charge or atomic multipole electrostatics. A default value of 5 is used in the absence of the PME-ORDER keyword.

.. index:: POLAR-12-INTRA
.. _KEY-POLAR-12-INTRA:

POLAR-12-INTRA [real]
   Provides a multiplicative scale factor that is applied to polarization interactions between 1-2 connected atoms located in the same polarization group. The default value of 0.0 is used, if the POLAR-12-INTRA keyword is not given in either the parameter file or the keyfile.

.. index:: POLAR-12-SCALE
.. _KEY-POLAR-12-SCALE:

POLAR-12-SCALE [real]
   Provides a multiplicative scale factor that is applied to polarization interactions between 1-2 connected atoms located in different polarization groups. The default value of 0.0 is used, if the POLAR-12-SCALE keyword is not given in either the parameter file or the keyfile.

.. index:: POLAR-13-INTRA
.. _KEY-POLAR-13-INTRA:

POLAR-13-INTRA [real]
   Provides a multiplicative scale factor that is applied to polarization interactions between 1-3 connected atoms located in the same polarization group. The default value of 0.0 is used, if the POLAR-13-INTRA keyword is not given in either the parameter file or the keyfile.

.. index:: POLAR-13-SCALE
.. _KEY-POLAR-13-SCALE:

POLAR-13-SCALE [real]
   Provides a multiplicative scale factor that is applied to polarization interactions between 1-3 connected atoms located in different polarization groups. The default value of 0.0 is used, if the POLAR-13-SCALE keyword is not given in either the parameter file or the keyfile.

.. index:: POLAR-14-INTRA
.. _KEY-POLAR-14-INTRA:

POLAR-14-INTRA [real]
   Provides a multiplicative scale factor that is applied to polarization interactions between 1-4 connected atoms located in the same polarization group. The default value of 0.5 is used, if the POLAR-14-INTRA keyword is not given in either the parameter file or the keyfile.

.. index:: POLAR-14-SCALE
.. _KEY-POLAR-14-SCALE:

POLAR-14-SCALE [real]
   Provides a multiplicative scale factor that is applied to polarization interactions between 1-4 connected atoms located in different polarization groups. The default value of 1.0 is used, if the POLAR-14-SCALE keyword is not given in either the parameter file or the keyfile.

.. index:: POLAR-15-INTRA
.. _KEY-POLAR-15-INTRA:

POLAR-15-INTRA [real]
   Provides a multiplicative scale factor that is applied to polarization interactions between 1-5 connected atoms located in the same polarization group. The default value of 1.0 is used, if the POLAR-15-INTRA keyword is not given in either the parameter file or the keyfile.

.. index:: POLAR-15-SCALE
.. _KEY-POLAR-15-SCALE:

POLAR-15-SCALE [real]
   Provides a multiplicative scale factor that is applied to polarization interactions between 1-5 connected atoms located in different polarization groups. The default value of 1.0 is used, if the POLAR-15-SCALE keyword is not given in either the parameter file or the keyfile.

.. index:: POLAR-EPS
.. _KEY-POLAR-EPS:

POLAR-EPS [real]
   Sets the convergence criterion applied during computation of self-consistent induced dipoles. The calculation is deemed to have converged when the rms change in Debyes in the induced dipole at all polarizable sites is less than the value specified with this keyword. The default value in the absence of the keyword is 0.000001 Debyes.

.. index:: POLAR-ITER
.. _KEY-POLAR-ITER:

POLAR-ITER
   Sets the maximum number of conjugate gradient iterations to be used in the solution of the self-consistent mutual induced dipoles. The default values in the absence of the keyword is 100 iterations.

.. index:: POLAR-PREDICT
.. _KEY-POLAR-PREDICT:

POLAR-PREDICT [ASPC/GEAR/LSQR]
   Turns on use of an induced dipole prediction method to accelerate convergence of self-consistent induced dipoles. The Always Stable Predictor-Corrector (ASPC) method, a standard Gear extrapolation method (GEAR), and extrapolation based on a least squared prediction (LSQR) are available as modifiers to the keyword. The default value if the keyword is used without a modifier is ASPC. Use of POLAR-PREDICT biases the early stages of induced dipole convergence, and should only be used when requesting tight convergence of 0.00001 or less via POLAR-EPS.

POLARIZABLE

.. index:: POLARIZATION
.. _KEY-POLARIZATION:

POLARIZATION [DIRECT/MUTUAL]
   Selects between the use of direct and mutual dipole polarization for force fields that incorporate the polarization term. The DIRECT modifier avoids an iterative calculation by using only the permanent electric field in computation of induced dipoles. The MUTUAL option, which is the default in the absence of the POLARIZATION keyword, iterates the induced dipoles to self-consistency.

.. index:: POLARIZE
.. _KEY-POLARIZE:

POLARIZE [1 integer, 1 real & up to 4 integers]
   Provides the values for a single atomic dipole polarizability parameter. The integer modifier, if positive, gives the atom type number for which a polarizability parameter is to be defined. If the first integer modifier is negative, then the parameter value to follow applies only to the individual atom whose atom number is the negative of the modifier. The real number modifier gives the value of the dipole polarizability in Ang^3. The final integer modifiers list the atom type numbers of atoms directly bonded to the current atom and which will be considered to be part of the current atom's polarization group.

.. index:: POLARIZETERM
.. _KEY-POLARIZETERM:

POLARIZETERM [NONE/ONLY]
   Controls use of the atomic dipole polarization potential energy term. In the absence of a modifying option, this keyword turns on use of the potential. The NONE option turns off use of this potential energy term. The ONLY option turns off all potential energy terms except for this one.

.. index:: POLYMER-CUTOFF
.. _KEY-POLYMER-CUTOFF:

POLYMER-CUTOFF [real]
   Sets the value of an additional cutoff parameter needed for infinite polymer systems. This value must be set to less than half the minimal periodic box dimension and should be greater than the largest possible interatomic distance that can be subject to scaling or exclusion as a local electrostatic or van der Waals interaction. The default in the absence of the POLYMER-CUTOFF keyword is 5.5 Angstroms.

POTENTIAL-ATOMS

POTENTIAL-FACTOR

POTENTIAL-FIT

POTENTIAL-OFFSET

POTENTIAL-SHELLS

POTENTIAL-SPACING

.. index:: PPME-ORDER
.. _KEY-PPME-ORDER:

PPME-ORDER [integer]
   Sets the order of the B-spline interpolation used during particle mesh Ewald summation for polarization interactions. A default value of 5 is used in the absence of the PPME-ORDER keyword.

.. index:: PRINTOUT
.. _KEY-PRINTOUT:

PRINTOUT [integer]
   Sets the number of iterations between writes of status information to the standard output for iterative procedures such as minimizations. The default value in the absence of the keyword is 1, i.e., the calculation status is given every iteration.

.. index:: RADIUSRULE
.. _KEY-RADIUSRULE:

RADIUSRULE [ARITHMETIC/GEOMETRIC/CUBIC-MEAN]
   Sets the functional form of the radius combining rule for heteroatomic van der Waals potential energy interactions. The default in the absence of the RADIUSRULE keyword is to use the arithmetic mean combining rule to get radii for heteroatomic interactions.

.. index:: RADIUSSIZE
.. _KEY-RADIUSSIZE:

RADIUSSIZE [RADIUS/DIAMETER]
   Determines whether the atom size values given in van der Waals parameters read from VDW keyword statements are interpreted as atomic radius or diameter values. The default in the absence of the RADIUSSIZE keyword is to assume that vdw size parameters are given as radius values.

.. index:: RADIUSTYPE
.. _KEY-RADIUSTYPE:

RADIUSTYPE [R-MIN/SIGMA]
   Determines whether atom size values given in van der Waals parameters read from VDW keyword statements are interpreted as potential minimum (Rmin) or LJ-style sigma values. The default in the absence of the RADIUSTYPE keyword is to assume that vdw size parameters are given as Rmin values.

.. index:: RANDOMSEED
.. _KEY-RANDOMSEED:

RANDOMSEED [integer]
   Followed by an integer value, sets the initial seed value for the random number generator used by Tinker. Setting RANDOMSEED to the same value as an earlier run will allow exact reproduction of the earlier calculation. (Note that this will not hold across different machine types.) RANDOMSEED should be set to a positive integer less than about 2 billion. In the absence of the RANDOMSEED keyword the seed is chosen "randomly" based upon the number of seconds that have elapsed in the current decade.

.. index:: RATTLE
.. _KEY-RATTLE:

RATTLE [BONDS/ANGLES/DIATOMIC/TRIATOMIC/WATER]
   Invokes the rattle algorithm, a velocity version of shake, on portions of a molecular system during a molecular dynamic calculation. The RATTLE keyword can be followed by any of the modifiers shown, in which case all occurrences of the modifier species are constrained at ideal values taken from the bond and angle parameters of the force field in use. In the absence of any modifier, RATTLE constrains all bonds to hydrogen atoms at ideal bond lengths.

.. index:: RATTLE-DISTANCE
.. _KEY-RATTLE-DISTANCE:

RATTLE-DISTANCE [2 integers]
   Allows the use of a holonomic constraint between the two atoms whose numbers are specified on the keyword line. If the two atoms are involved in a covalent bond, then their distance is constrained to the ideal bond length from the force field. For nonbonded atoms, the rattle constraint is fixed at their distance in the input coordinate file.

RATTLE-EPS

RATTLE-LINE [integer]

RATTLE-ORIGIN [integer]

RATTLE-PLANE [integer]

.. index:: REACTIONFIELD
.. _KEY-REACTIONFIELD:

REACTIONFIELD [2 reals & 1 integer]
   Provides parameters needed for the reaction field potential energy calculation. The two real modifiers give the radius of the dielectric cavity and the ratio of the bulk dielectric outside the cavity to that inside the cavity. The integer modifier gives the number of terms in the reaction field summation to be used. In the absence of the REACTIONFIELD keyword, the default values are a cavity of radius 1000000 Ang, a dielectric ratio of 80 and use of only the first term of the reaction field summation.

.. index:: REDUCE
.. _KEY-REDUCE:

REDUCE [real]
   Specifies the fraction between zero and one by which the path between starting and final conformational state will be shortened at each major cycle of the transition state location algorithm implemented by the SADDLE program. This causes the path endpoints to move up and out of the terminal structures toward the transition state region. In favorable cases, a nonzero value of the REDUCE modifier can speed convergence to the transition state. The default value in the absence of the REDUCE keyword is zero.

.. index:: REMOVE-INERTIA
.. _KEY-REMOVE-INERTIA:

REMOVE-INERTIA [integer]
   Specifies the number of molecular dynamics steps between removal of overall tranlational and/or rotational motion of the system. The default value in the absence of the REMOVE-INERTIA keyword is 100 steps.

REP-12-SCALE

REP-13-SCALE

REP-14-SCALE

REP-15-SCALE

.. index:: REPULS-CUTOFF
.. _KEY-REPULS-CUTOFF:

REPULS-CUTOFF [real]
   Sets the cutoff distance value in Angstroms for Pauli repulsion potential energy interactions. The energy for any pair of sites beyond the cutoff distance will be set to zero. Other keywords can be used to select a smoothing scheme near the cutoff distance. The default cutoff distance in the absence of the REPULS-CUTOFF keyword is 6.0 Angstroms.

.. index:: REPULS-TAPER
.. _KEY-REPULS-TAPER:

REPULS-TAPER [real]
   Modifies the cutoff window for Pauli repulsion energy interactions. It is similar in form and action to the TAPER keyword, except that its value applies only to the Pauli repulsion potential. The default value in the absence of the REPULS-TAPER keyword is to begin the cutoff window at 0.9 of the corresponding cutoff distance.

REPULSION

.. index:: REPULSIONTERM
.. _KEY-REPULSIONTERM:

REPULSIONTERM [NONE/ONLY]
   Controls use of the Pauli repulsion potential energy term. In the absence of a modifying option, this keyword turns on use of the potential. The NONE option turns off use of this potential energy term. The ONLY option turns off all potential energy terms except for this one.

RESP-WEIGHT

RESPA-INNER

RESPTYPE

.. index:: RESTRAIN-ANGLE
.. _KEY-RESTRAIN-ANGLE:

RESTRAIN-ANGLE [3 integers & 3 reals]
   Implements a flat-welled harmonic potential that can be used to restrain the angle between three atoms to lie within a specified angle range. The integer modifiers contain the atom numbers of the three atoms whose angle is to be restrained.  The first real modifier is the force constant in kcal/radian^2 for the restraint. The last two real modifiers give the lower and upper bounds in degrees on the allowed angle values. If the angle lies between the lower and upper bounds, the restraint potential is zero. Outside the bounds, the harmonic restraint is applied. If the angle range modifiers are omitted, then the atoms are restrained to the angle found in the input structure. If the force constant is also omitted, a default value of 10.0 is used.

.. index:: RESTRAIN-DISTANCE
.. _KEY-RESTRAIN-DISTANCE:

RESTRAIN-DISTANCE [2 integers & 3 reals]
   Implements a flat-welled harmonic potential that can be used to restrain two atoms to lie within a specified distance range. The integer modifiers contain the atom numbers of the two atoms to be restrained. The first real modifier specifies the force constant in kcal/Ang^2 for the restraint. The next two real modifiers give the lower and upper bounds in Angstroms on the allowed distance range. If the interatomic distance lies between these lower and upper bounds, the restraint potential is zero. Outside the bounds, the harmonic restraint is applied. If the distance range modifiers are omitted, then the atoms are restrained to the interatomic distance found in the input structure. If the force constant is also omitted, a default value of 100.0 is used.

.. index:: RESTRAIN-GROUPS
.. _KEY-RESTRAIN-GROUPS:

RESTRAIN-GROUPS [2 integers & 3 reals]
   Implements a flat-welled harmonic distance restraint between the centers-of-mass of two groups of atoms. The integer modifiers are the numbers of the two groups which must be defined separately via the GROUP keyword. The first real modifier is the force constant in kcal/Ang^2 for the restraint. The last two real modifiers give the lower and upper bounds in Angstroms on the allowed intergroup center-of-mass distance values. If the distance range modifiers are omitted, then the groups are restrained to the distance found in the input structure. If the force constant is also omitted, a default value of 100.0 is used.

.. index:: RESTRAIN-PLANE
.. _KEY-RESTRAIN-PLANE:

RESTRAIN-PLANE [X/Y/Z, 1 integer & 3 reals]
   Provides the ability to restrain an individual atom to a specified plane orthogonal to a coordinate axis. The first modifier gives the axis (X, Y or Z) perpendicular to the restraint plane. The integer modifier contains the atom number of the atom to be restrained. The first real number modifier gives the coordinate value to which the atom is restrained along the specified axis. The second real modifier sets the force constant in kcal/Ang^2 for the harmonic restraint potential. The final real modifier defines a range above and below the specified plane within which the restraint value is zero. If the force constant is omitted, a default value of 100.0 is used. If the exclusion range is omitted, it is taken to be zero.

.. index:: RESTRAIN-POSITION
.. _KEY-RESTRAIN-POSITION:

RESTRAIN-POSITION [1 integer & 5 reals, OR 2 integers & 2 reals]
   Provides the ability to restrain an atom or group of atoms to specified coordinate positions. An initial positive integer modifier contains the atom number of the atom to be restrained. The first three real number modifiers give the X-, Y- and Z-coordinates to which the atom is tethered. The fourth real modifier sets the force constant in kcal/Ang^2 for the harmonic restraint potential. The final real modifier defines a sphere around the specified coordinates within which the restraint value is zero. If the coordinates are omitted, then the atom is restrained to the origin. If the force constant is omitted, a default value of 100.0 is used. If the exclusion sphere radius is omitted, it is taken to be zero.

Alternatively, if the initial integer modifier is negative, then a second integer is read, followed by two real number modifiers. All atoms in the range from the absolute value of the first integer through the second integer are restrained to their current coordinates. The first real modifier is the harmonic force constant in kcal/Ang^2, and the second real defines a sphere around each atom within which the restraint value is zero. If the force constant is omitted, a default value of 100.0 is used. If the exclusion sphere radius is omitted, it is taken to be zero.

.. index:: RESTRAIN-TORSION
.. _KEY-RESTRAIN-TORSION:

RESTRAIN-TORSION [4 integers & 3 reals]
   Implements a flat-welled harmonic potential that can be used to restrain the torsional angle between four atoms to lie within a specified angle range. The initial integer modifiers contains the atom numbers of the four atoms whose torsional angle, computed in the atom order listed, is to be restrained. The first real modifier gives a force constant in kcal/radian^2 for the restraint. The last two real modifiers give the lower and upper bounds in degrees on the allowed torsional angle values. The angle values given can wrap around across -180 and +180 degrees. Outside the allowed angle range, the harmonic restraint is applied. If the angle range modifiers are omitted, then the atoms are restrained to the torsional angle found in the input structure. If the force constant is also omitted, a default value of 1.0 is used.

.. index:: RESTRAINTERM
.. _KEY-RESTRAINTERM:

RESTRAINTERM [NONE/ONLY]
   Controls use of the restraint potential energy terms. In the absence of a modifying option, this keyword turns on use of these potentials. The NONE option turns off use of these potential energy terms. The ONLY option turns off all potential energy terms except for these terms.

ROTATABLE-BOND

.. index:: RXNFIELDTERM
.. _KEY-RXNFIELDTERM:

RXNFIELDTERM [NONE/ONLY]
   Controls use of the reaction field continuum solvation potential energy term. In the absence of a modifying option, this keyword turns on use of the potential. The NONE option turns off use of this potential energy term. The ONLY option turns off all potential energy terms except for this one.

.. index:: SADDLEPOINT
.. _KEY-SADDLEPOINT:

SADDLEPOINT
   Allows Newton-style second derivative-based optimization routine used by NEWTON, NEWTROT and other programs to converge to saddlepoints as well as minima on the potential surface. By default, in the absence of the SADDLEPOINT keyword, checks are applied that prevent convergence to stationary points having directions of negative curvature.

.. index:: SAVE-CYCLE
.. _KEY-SAVE-CYCLE:

SAVE-CYCLE
   Causes Tinker programs, such as minimizations and molecular dynamics, that output intermediate coordinate sets to save each successive set to the next consecutively numbered cycle file. The SAVE-CYCLE keyword is the opposite of the OVERWRITE keyword.

.. index:: SAVE-FORCE
.. _KEY-SAVE-FORCE:

SAVE-FORCE
   Causes Tinker molecular dynamics calculations to save the values of the force components on each atom to a separate cycle file. These files are written whenever the atomic coordinate snapshots are written during the dynamics run. Each atomic force file name contains as a suffix the cycle number followed by the letter "f".

.. index:: SAVE-INDUCED
.. _KEY-SAVE-INDUCED:

SAVE-INDUCED
   Causes Tinker molecular dynamics calculations that involve polarizable atomic multipoles to save the values of the induced dipole components on each polarizable atom to a separate cycle file. These files are written whenever the atomic coordinate snapshots are written during the dynamics run. Each induced dipole file name contains as a suffix the cycle number followed by the letter "u".

.. index:: SAVE-VECTS
.. _KEY-SAVE-VECTS:

SAVE-VECTS [integer]
   Specifies the number of iterations between the saving of restart vectors during block iterative determination of the low frequence vibrational modes. A default value of 10 is used for SAVE-VECTS in the absence of the keyword.

.. index:: SAVE-VELOCITY
.. _KEY-SAVE-VELOCITY:

SAVE-VELOCITY
   Causes Tinker molecular dynamics calculations to save the values of the velocity components on each atom to a separate cycle file. These files are written whenever the atomic coordinate snapshots are written during the dynamics run. Each velocity file name contains as a suffix the cycle number followed by the letter "v".

.. index:: SLOPEMAX
.. _KEY-SLOPEMAX:

SLOPEMAX [real]
   Sets via its modifying value the maximum allowed size of the ratio between the current and initial projected gradients during the line search phase of conjugate gradient or truncated Newton optimizations. If this ratio exceeds SLOPEMAX, then the initial step size is reduced by a factor of 10. The default value is usually set to 10000.0 when not specified via the SLOPEMAX keyword.

.. index:: SMOOTHING
.. _KEY-SMOOTHING:

SMOOTHING [DEM/GDA/TOPHAT/STOPHAT]
   Activates the potential energy smoothing methods. Several variations are available depending on the value of the modifier used: DEM= Diffusion Equation Method with a standard Gaussian kernel; GDA= Gaussian Density Annealing as proposed by the Straub group; TOPHAT= a local DEM-like method using a finite range "tophat" kernel; STOPHAT= shifted tophat smoothing.

.. index:: SOLVATE
.. _KEY-SOLVATE:

SOLVATE [ASP/SASA/ONION/STILL/HCT/OCB/ACE/GB/GB-HPMF/GK/GK-HMPF/PB/PB-HMPF]
   Turns on a continuum solvation free energy term during energy calculations when used with standard force fields. Several algorithms are available based on the modifier used: ASP is the Eisenberg-McLachlan ASP method using the Wesson-Eisenberg vacuum-to-water parameters, SASA is the Ooi-Scheraga SASA method, ONION is the original 1990 Still "Onion-shell" GB/SA method, STILL is the 1997 analytical GB/SA method from Still's group, HCT is the pairwise descreening method of Hawkins, Cramer and Truhlar, OBC is the Onufriev-Bashford-Case method, ACE is the Analytical Continuum Electrostatics method from Karplus' group, GB is equivalent to the STILL modifier, GK is the Generalized Kirkwood method for polarizable multipoles, and PB is a Poisson-Boltzmann method using APBS. The HPMF versions use Head-Gordon's Hydrophobic Potential of Mean Force method as the non-electrostatic component.

.. index:: SOLVATETERM
.. _KEY-SOLVATETERM:

SOLVATETERM [NONE/ONLY]
   Controls use of the macroscopic solvation potential energy term. In the absence of a modifying option, this keyword turns on use of the potential. The NONE option turns off use of this potential energy term. The ONLY option turns off all potential energy terms except for this one.

SOLVENT-PRESSURE

.. index:: SPACEGROUP
.. _KEY-SPACEGROUP:

SPACEGROUP [name]
   Selects the space group to be used in manipulation of crystal unit cells and asymmetric units. The name option must be chosen from one of the currently implemented space groups, which include about 90 of the most common space groups out of the total of 230 possibilities.

.. index:: STEEPEST-DESCENT
.. _KEY-STEEPEST-DESCENT:

STEEPEST-DESCENT
   Forces the L-BFGS optimization routine used by the MINIMIZE program and other programs to perform steepest descent minimization. This option can be useful in conjunction with small step sizes for following minimum energy paths, but is generally inferior to the L-BFGS default for most optimization purposes.

.. index:: STEPMAX
.. _KEY-STEPMAX:

STEPMAX [real]
   Sets via its modifying value the maximum size of an individual step during the line search phase of conjugate gradient or truncated Newton optimizations. The step size is computed as the norm of the vector of changes in parameters being optimized. The default value depends on the particular Tinker program, but is usually in the range from 1.0 to 5.0 when not specified via the STEPMAX keyword.

.. index:: STEPMIN
.. _KEY-STEPMIN:

STEPMIN [real]
   Sets via its modifying value the minimum size of an individual step during the line search phase of conjugate gradient or truncated Newton optimizations. The step size is computed as the norm of the vector of changes in parameters being optimized. The default value is usually set to about 10-16 when not specified via the STEPMIN keyword.

.. index:: STRBND
.. _KEY-STRBND:

STRBND [3 integers & 2 reals]
   Provides the values for a single stretch-bend cross term potential parameter. The integer modifiers give the atom class numbers for the three kinds of atoms involved in the angle which is to be defined. The real number modifiers give the force constant values for the first bond (first two atom classes) with the angle, and the second bond with the angle, respectively. The default units for the stretch-bend force constant are kcal/mole/Ang-radian, but this can be controlled via the STRBNDUNIT keyword.

.. index:: STRBNDTERM
.. _KEY-STRBNDTERM:

STRBNDTERM [NONE/ONLY]
   Controls use of the bond stretching-angle bending cross term potential energy. In the absence of a modifying option, this keyword turns on use of the potential. The NONE option turns off use of this potential energy term. The ONLY option turns off all potential energy terms except for this one.

.. index:: STRBNDUNIT
.. _KEY-STRBNDUNIT:

STRBNDUNIT [real]
   Sets the scale factor needed to convert the energy value computed by the bond stretching-angle bending cross term potential into units of kcal/mole. The correct value is force field dependent and typically provided in the header of the master force field parameter file. The default value of (Pi/180) = 0.0174533 is used, if the STRBNDUNIT keyword is not given in the force field parameter file or the keyfile.

.. index:: STRTORS
.. _KEY-STRTORS:

STRTORS [2 integers & 1 real]
   Provides the values for a single stretch-torsion cross term potential parameter. The two integer modifiers give the atom class numbers for the atoms involved in the central bond of the torsional angles to be parameterized. The real modifier gives the value of the stretch-torsion force constant for all torsional angles with the defined atom classes for the central bond. The default units for the stretch-torsion force constant can be controlled via the STRTORUNIT keyword.

.. index:: STRTORTERM
.. _KEY-STRTORTERM:

STRTORTERM [NONE/ONLY]
   Controls use of the bond stretching-torsional angle cross term potential energy. In the absence of a modifying option, this keyword turns on use of the potential. The NONE option turns off use of this potential energy term. The ONLY option turns off all potential energy terms except for this one.

.. index:: STRTORUNIT
.. _KEY-STRTORUNIT:

STRTORUNIT [real]
   Sets the scale factor needed to convert the energy value computed by the bond stretching-torsional angle cross term potential into units of kcal/mole. The correct value is force field dependent and typically provided in the header of the master force field parameter file. The default value of 1.0 is used, if the STRTORUNIT keyword is not given in the force field parameter file or the keyfile.

SURFACE-TENSION

.. index:: TAPER
.. _KEY-TAPER:

TAPER [real]
   Allows modification of the cutoff windows for nonbonded potential energy interactions. The nonbonded terms are smoothly reduced from their standard value at the beginning of the cutoff window to zero at the far end of the window. The far end of the window is specified via the CUTOFF keyword or its potential function specific variants. The modifier value supplied with the TAPER keyword sets the beginning of the cutoff window. The modifier can be given either as an absolute distance value in Angstroms, or as a fraction between zero and one of the CUTOFF distance. The default value in the absence of the TAPER keyword ranges from 0.65 to 0.9 of the CUTOFF distance depending on the type of potential function. The windows are implemented via polynomial-based switching functions, in some cases combined with energy shifting.

TARGET-DIPOLE

TARGET-QUADRUPOLE

.. index:: TAU-PRESSURE
.. _KEY-TAU-PRESSURE:

TAU-PRESSURE [real]
   Sets the coupling time in picoseconds for the Groningen-style pressure bath coupling used to control the system pressure during molecular dynamics calculations. A default value of 2.0 is used for TAU-PRESSURE in the absence of the keyword.

.. index:: TAU-TEMPERATURE
.. _KEY-TAU-TEMPERATURE:

TAU-TEMPERATURE [real]
   Sets the coupling time in picoseconds for the Groningen-style temperature bath coupling used to control the system temperature during molecular dynamics calculations. A default value of 0.1 is used for TAU-TEMPERATURE in the absence of the keyword.

TCG-GUESS

TCG-NOGUESS

TCG-PEEK

.. index:: THERMOSTAT
.. _KEY-THERMOSTAT:

THERMOSTAT [BUSSI/BERENDSEN/ANDERSEN/NOSE-HOOVER]
   Selects a thermostat algorithm for use during molecular dynamics. Four modifiers are available: BUSSI is a Bussi-Parrinello stochastic coupling method, BERENSDEN is the original Berendsen bath coupling method, ANDERSEN is the Andersen stochastic collision method, and NOSE-HOOVER is a Nose-Hoover extended variable chain method. The default in the absence of the THERMOSTAT keyword is to use the BUSSI method.

.. index:: TORS-LAMBDA
.. _KEY-TORS-LAMBDA:

TORS-LAMBDA [real]
   Sets the value of the lambda scaling parameters for torsional interactions during free energy calculations and similar. The real number modifier sets the position along path from the initial state (lambda=0) to the final state (lambda=1). Alternatively, this parameter can set the state of annihilation for specified torsional interactions from none (lambda=1) to complete (lambda=0). The torsions involved in the scaling are given separately via ROTATABLE-BOND keywords.

.. index:: TORSION
.. _KEY-TORSION:

TORSION [4 integers & up to 6 real/real/integer triples]
   Provides the values for a single torsional angle parameter. The first four integer modifiers give the atom class numbers for the atoms involved in the torsional angle to be defined. Each of the remaining triples of real/real/integer modifiers give the amplitude, phase offset in degrees and periodicity of a particular torsional function term, respectively. Periodicities through 6-fold are allowed for torsional parameters.

.. index:: TORSION4
.. _KEY-TORSION4:

TORSION4 [4 integers & up to 6 real/real/integer triples]
   Provides the values for a single torsional angle parameter specific to atoms in 4-membered rings. The first four integer modifiers give the atom class numbers for the atoms involved in the torsional angle to be defined. The remaining triples of real number and integer modifiers operate as described above for the TORSION keyword.

.. index:: TORSION5
.. _KEY-TORSION5:

TORSION5 [4 integers & up to 6 real/real/integer triples]
   Provides the values for a single torsional angle parameter specific to atoms in 5-membered rings. The first four integer modifiers give the atom class numbers for the atoms involved in the torsional angle to be defined. The remaining triples of real number and integer modifiers operate as described above for the TORSION keyword.

.. index:: TORSIONTERM
.. _KEY-TORSIONTERM:

TORSIONTERM [NONE/ONLY]
   Controls use of the torsional angle potential energy term. In the absence of a modifying option, this keyword turns on use of the potential. The NONE option turns off use of this potential energy term. The ONLY option turns off all potential energy terms except for this one.

.. index:: TORSIONUNIT
.. _KEY-TORSIONUNIT:

TORSIONUNIT [real]
   Sets the scale factor needed to convert the energy value computed by the torsional angle potential into units of kcal/mole. The correct value is force field dependent and typically provided in the header of the master force field parameter file. The default value of 1.0 is used, if the TORSIONUNIT keyword is not given in the force field parameter file or the keyfile.

.. index:: TORTORS
.. _KEY-TORTORS:

TORTORS [7 integers, then multiple lines of 2 integers and 1 real]
   Provides the values for a single torsion-torsion parameter. The first five integer modifiers give the atom class numbers for the atoms involved in the two adjacent torsional angles to be defined. The last two integer modifiers contain the number of data grid points that lie along each axis of the torsion-torsion map. For example, this value will be 13 for a 30 degree torsional angle spacing, i.e., 360/30 = 12, but 13 values are required since data values for -180 and +180 degrees must both be supplied. The subsequent lines contain the torsion-torsion map data as the integer values in degrees of each torsional angle and the target energy value in kcal/mole.

.. index:: TORTORTERM
.. _KEY-TORTORTERM:

TORTORTERM [NONE/ONLY]
   Controls use of the torsion-torsion potential energy term. In the absence of a modifying option, this keyword turns on use of the potential. The NONE option turns off use of this potential energy term. The ONLY option turns off all potential energy terms except for this one.

.. index:: TORTORUNIT
.. _KEY-TORTORUNIT:

TORTORUNIT [real]
   Sets the scale factor needed to convert the energy value computed by the torsion-torsion potential into units of kcal/mole. The correct value is force field dependent and typically provided in the header of the master force field parameter file. The default value of 1.0 is used, if the TORTORUNIT keyword is not given in the force field parameter file or the keyfile.

.. index:: TRIAL-DISTANCE
.. _KEY-TRIAL-DISTANCE:

TRIAL-DISTANCE [CLASSIC/RANDOM/TRICOR/HAVEL integer/PAIRWISE integer]
   Sets the method for selection of a trial distance matrix during distance geometry computations. The keyword takes a modifier that selects the method to be used. The HAVEL and PAIRWISE modifiers also require an additional integer value that specifies the number of atoms used in metrization and the percentage of metrization, respectively. The default in the absence of this keyword is to use the PAIRWISE method with 100 percent metrization. Further information on the various methods is given with the description of the Tinker distance geometry program.

.. index:: TRIAL-DISTRIBUTION
.. _KEY-TRIAL-DISTRIBUTION:

TRIAL-DISTRIBUTION [real]
   Sets the initial value for the mean of the Gaussian distribution used to select trial distances between the lower and upper bounds during distance geometry computations. The value given must be between 0 and 1 which represent the lower and upper bounds respectively. This keyword is rarely needed since Tinker will usually be able to choose a reasonable value by default.

.. index:: TRUNCATE
.. _KEY-TRUNCATE:

TRUNCATE
   Causes all distance-based nonbond energy cutoffs to be sharply truncated to an energy of zero at distances greater than the value set by the cutoff keyword(s) without use of any shifting, switching or smoothing schemes. At all distances within the cutoff sphere, the full interaction energy is computed.

.. index:: UREY-CUBIC
.. _KEY-UREY-CUBIC:

UREY-CUBIC [real]
   Sets the value of the cubic term in the Taylor series expansion form of the Urey-Bradley potential energy. The real number modifier gives the value of the coefficient as a multiple of the quadratic coefficient. The default value in the absence of the UREY-CUBIC keyword is zero; i.e., the cubic Urey-Bradley term is omitted.

.. index:: UREY-QUARTIC
.. _KEY-UREY-QUARTIC:

UREY-QUARTIC [real]
   Sets the value of the quartic term in the Taylor series expansion form of the Urey-Bradley potential energy. The real number modifier gives the value of the coefficient as a multiple of the quadratic coefficient. The default value in the absence of the UREY-QUARTIC keyword is zero; i.e., the quartic Urey-Bradley term is omitted.

.. index:: UREYBRAD
.. _KEY-UREYBRAD:

UREYBRAD [3 integers & 2 reals]
   Provides the values for a single Urey-Bradley cross term potential parameter. The integer modifiers give the atom class numbers for the three kinds of atoms involved in the angle for which a Urey-Bradley term is to be defined. The real number modifiers give the force constant value for the term and the target value for the 1-3 distance in Angstroms. The default units for the force constant are kcal/mole/Ang^2, but this can be controlled via the UREYUNIT keyword.

.. index:: UREYTERM
.. _KEY-UREYTERM:

UREYTERM [NONE/ONLY]
   Controls use of the Urey-Bradley potential energy term. In the absence of a modifying option, this keyword turns on use of the potential. The NONE option turns off use of this potential energy term. The ONLY option turns off all potential energy terms except for this one.

.. index:: UREYUNIT
.. _KEY-UREYUNIT:

UREYUNIT [real]
   Sets the scale factor needed to convert the energy value computed by the Urey-Bradley potential into units of kcal/mole. The correct value is force field dependent and typically provided in the header of the master force field parameter file. The default value of 1.0 is used, if the UREYUNIT keyword is not given in the force field parameter file or the keyfile.

.. index:: USOLVE-BUFFER
.. _KEY-USOLVE-BUFFER:

USOLVE-BUFFER [real]
   Sets the size of the neighbor list buffer in Angstroms for the sparse conjugate gradient preconditioner used in computing induced dipoles. This value is added to the actual cutoff distance to determine which pairs will be kept on the neighbor list. The default value in the absence of the USOLVE-BUFFER keyword is 2.0 Angstroms.

.. index:: USOLVE-CUTOFF
.. _KEY-USOLVE-CUTOFF:

USOLVE-CUTOFF [real]
   Sets the cutoff distance value in Angstroms for the sparse conjugate gradient preconditioner used in computing induced dipoles. The default cutoff distance in the absence of the USOLVE-CUTOFF keyword is 4.5 Angstroms.

.. index:: USOLVE-DIAG
.. _KEY-USOLVE-DIAG:

USOLVE-DIAG [real]
   Sets the multiplicative acceleration factor applied to the diagonal elements of the sparse preconditioner used during conjugate gradient solution of induced dipoles. The default value of 2.0 is used in the absence of the USOLVE-DIAG keyword.

.. index:: VDW
.. _KEY-VDW:

VDW [1 integer & 3 reals]
   Provides values for a single van der Waals parameter. The integer modifier, if positive, gives the atom class number for which vdw parameters are to be defined. Note that vdw parameters are given for atom classes, not atom types. The three real number modifiers give the values of the atom size in Angstroms, homoatomic well depth in kcal/mole, and an optional reduction factor for univalent atoms.

.. index:: VDW-12-SCALE
.. _KEY-VDW-12-SCALE:

VDW-12-SCALE [real]
   Provides a multiplicative scale factor that is applied to van der Waals potential interactions between 1-2 connected atoms, i.e., atoms that are directly bonded. The default value of 0.0 is used, if the VDW-12-SCALE keyword is not given in either the parameter file or the keyfile.

.. index:: VDW-13-SCALE
.. _KEY-VDW-13-SCALE:

VDW-13-SCALE [real]
   Provides a multiplicative scale factor that is applied to van der Waals potential interactions between 1-3 connected atoms, i.e., atoms separated by two covalent bonds. The default value of 0.0 is used, if the VDW-13-SCALE keyword is not given in either the parameter file or the keyfile.

.. index:: VDW-14-SCALE
.. _KEY-VDW-14-SCALE:

VDW-14-SCALE [real]
   Provides a multiplicative scale factor that is applied to van der Waals potential interactions between 1-4 connected atoms, i.e., atoms separated by three covalent bonds. The default value of 1.0 is used, if the VDW-14-SCALE keyword is not given in either the parameter file or the keyfile.

.. index:: VDW-15-SCALE
.. _KEY-VDW-15-SCALE:

VDW-15-SCALE [real]
   Provides a multiplicative scale factor that is applied to van der Waals potential interactions between 1-5 connected atoms, i.e., atoms separated by four covalent bonds. The default value of 1.0 is used, if the VDW-15-SCALE keyword is not given in either the parameter file or the keyfile.

.. index:: VDW-ANNIHILATE
.. _KEY-VDW-ANNIHILATE:

VDW-ANNIHILATE
   Specifies van der Waals interactions will be annihilated instead of decoupled during free energy calculations based on the vdw "lambda" value. In decoupling the intra-ligand interactions remain fully present regardless of the "lambda" value, while in annihilation the "lambda" value is applied to intra-ligand interactions. The default in the absence of the VDW-ANNIHILATE keyword is to decouple van der Waals interactions between the mutated atoms or ligand and the rest of the system.

.. index:: VDW-CORRECTION
.. _KEY-VDW-CORRECTION:

VDW-CORRECTION
   Turns on the use of an isotropic long-range correction term to approximately account for van der Waals interactions beyond the cutoff distance. This correction modifies the value of the van der Waals energy and virial due to van der Waals interactions, but has no effect on the gradient of the van der Waals energy.

.. index:: VDW-CUTOFF
.. _KEY-VDW-CUTOFF:

VDW-CUTOFF [real]
   Sets the cutoff distance value in Angstroms for van der Waals potential energy interactions. The energy for any pair of van der Waals sites beyond the cutoff distance will be set to zero. Other keywords can be used to select a smoothing scheme near the cutoff distance. The default cutoff distance in the absence of the VDW-CUTOFF keyword is infinite for nonperiodic systems and 9.0 for periodic systems.

.. index:: VDW-LAMBDA
.. _KEY-VDW-LAMBDA:

VDW-LAMBDA [real]
   Sets the value of the lambda scaling parameters for vdw interactions during free energy calculations and similar. The real number modifier sets the position along path from the initial state (lambda=0) to the final state (lambda=1). Alternatively, this parameter can set the state of decoupling or annihilation for specified groups from none (lambda=1) to complete (lambda=0). The groups involved in the scaling are given separately via LIGAND or MUTATE keywords.

.. index:: VDW-LIST
.. _KEY-VDW-LIST:

VDW-LIST
   Turns on pairwise neighbor lists for any of the van der Waals potentials. This method will yield identical energetic results to the standard double loop method.

.. index:: VDW-TAPER
.. _KEY-VDW-TAPER:

VDW-TAPER [real]
   Allows modification of the cutoff windows for van der Waals potential energy interactions. It is similar in form and action to the TAPER keyword, except that its value applies only to the vdw potential. The default value in the absence of the VDW-TAPER keyword is to begin the cutoff window at 0.9 of the vdw cutoff distance.

.. index:: VDW14
.. _KEY-VDW14:

VDW14 [1 integer & 2 reals]
   Provides values for a single van der Waals parameter for use in 1-4 nonbonded interactions. The integer modifier, if positive, gives the atom class number for which vdw parameters are to be defined. Note that vdw parameters are given for atom classes, not atom types. The two real number modifiers give the values of the atom size in Angstroms and the homoatomic well depth in kcal/mole. Reduction factors, if used, are carried over from the VDW keyword for the same atom class.

VDWINDEX

.. index:: VDWPR
.. _KEY-VDWPR:

VDWPR [2 integers & 2 reals]
   Provides the values for the vdw parameters for a single special heteroatomic pair of atoms. The integer modifiers give the pair of atom class numbers for which special vdw parameters are to be defined. The two real number modifiers give the values of the minimum energy contact distance in Angstroms and the well depth at the minimum distance in kcal/mole.

.. index:: VDWTERM
.. _KEY-VDWTERM:

VDWTERM [NONE/ONLY]
   Controls use of the van der Waals repulsion-dispersion potential energy term. In the absence of a modifying option, this keyword turns on use of the potential. The NONE option turns off use of this potential energy term. The ONLY option turns off all potential energy terms except for this one.

.. index:: VDWTYPE
.. _KEY-VDWTYPE:

VDWTYPE [LENNARD-JONES/BUCKINGHAM/BUFFERED-14-7/MM3-HBOND/GAUSSIAN]
   Sets the functional form for the van der Waals potential energy term. The text modifier gives the name of the functional form to be used. The GAUSSIAN modifier value implements a two or four Gaussian fit to the corresponding Lennard-Jones function for use with potential energy smoothing schemes. The default in the absence of the VDWTYPE keyword is to use the standard two parameter Lennard-Jones function.

.. index:: VERBOSE
.. _KEY-VERBOSE:

VERBOSE
   Turns on printing of secondary and informational output during a variety of Tinker computations; a subset of the more extensive output provided by the DEBUG keyword.

VIB-ROOTS

VIB-TOLERANCE

.. index:: VOLUME-MOVE
.. _KEY-VOLUME-MOVE:

VOLUME-MOVE [real]
   Specifies the maximum magnitude in Ang^3 of a trial change in the periodic box size when using a Monte Carlo barostat. The default value of 100.0 Ang^3 is used in the absence of the VOLUME-MOVE keyword.

.. index:: VOLUME-SCALE
.. _KEY-VOLUME-SCALE:

VOLUME-SCALE [MOLECULAR/ATOMIC]
   Specifies the type of coordinate scaling to be used when making trial periodic box volume size changes during use of a Monte Carlo barostat. The MOLECULAR modifier enforces rigid body translation of molecules based on center of mass, while the ATOMIC value treats all coordinates independently. The default in the absence of the VOLUME-SCALE keyword is to use MOLECULAR scaling.

.. index:: VOLUME-TRIAL
.. _KEY-VOLUME-TRIAL:

VOLUME-TRIAL [integer]
   Specifies the average number of molecular dynamics steps between attempts to change the periodic box size when using a Monte Carlo barostat. The default value of 25 steps is used in the absence of the VOLUME-TRIAL keyword.

.. index:: WALL
.. _KEY-WALL:

WALL [real]
   Sets the radius of a spherical boundary used to maintain droplet boundary conditions. The real modifier specifies the desired approximate radius of the droplet. In practice, an artificial van der Waals wall is constructed at a fixed buffer distance of 2.5 Angstroms outside the specified radius. The effect is that atoms which attempt to move outside the region defined by the droplet radius will be forced toward the center.

.. index:: WRITEOUT
.. _KEY-WRITEOUT:

WRITEOUT [integer]
   Sets the number of iterations between writes of intermediate results (such as the current coordinates) to disk file(s) for iterative procedures such as minimizations. The default value in the absence of the keyword is 1, i.e., the intermediate results are written to file on every iteration. Whether successive intermediate results are saved to new files or replace previously written intermediate results is controlled by the OVERWRITE and SAVE-CYCLE keywords.

.. index:: X-AXIS
.. _KEY-X-AXIS:

X-AXIS [real]
   Sets the value of the a-axis length for a crystal unit cell, or, equivalently, the X-axis length for a periodic box. The length value in Angstroms is listed after the keyword. Equivalent to the A-AXIS keyword.

.. index:: Y-AXIS
.. _KEY-Y-AXIS:

Y-AXIS [real]
   Sets the value of the b-axis length for a crystal unit cell, or, equivalently, the Y-axis length for a periodic box. The length value in Angstroms is listed after the keyword. If the keyword is absent, the Y-axis length is set equal to the X-axis length. Equivalent to the B-AXIS keyword.

.. index:: Z-AXIS
.. _KEY-Z-AXIS:

Z-AXIS [real]
   Sets the value of the c-axis length for a crystal unit cell, or, equivalently, the Z-axis length for a periodic box. The length value in Angstroms is listed after the keyword. If the keyword is absent, the Z-axis length is set equal to the X-axis length. Equivalent to the C-AXIS keyword.
