//----------------------------------------------------------------------//

function t9_download(filename, text)
{
   var element = document.createElement('a');
   element.setAttribute(
      'href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(text));
   element.setAttribute('download', filename);
   element.style.display = 'none';
   document.body.appendChild(element);
   element.click();
   document.body.removeChild(element);
}

// today
const t9_month_abbrev = [
   "Jan.", "Feb.", "Mar.", "Apr.", "May", "June", "July", "Aug.", "Sept.",
   "Oct.", "Nov.", "Dec."
];
let t9_today = new Date();
let t9_accessed_year = t9_today.getFullYear();
let t9_accessed_month = t9_month_abbrev[t9_today.getMonth()];
let t9_accessed_month_num = t9_today.getMonth() + 1;
let t9_accessed_date = t9_today.getDate();
function t9_accessed_bibtex()
{
   return `${t9_accessed_month} ${t9_accessed_date}, ${t9_accessed_year}`;
}
function t9_accessed_ris()
{
   return `${t9_accessed_year}/${t9_accessed_month_num}/${t9_accessed_date}/`;
}

//----------------------------------------------------------------------//

// Tinker9 on GitHub: bib

const t9_github_bib = `@misc {Tinker9_GitHub,
author = {Wang, Zhi},
title = {{Tinker9: Next Generation of Tinker with GPU Support}},
shorttitle = {{Tinker9}},
year = {2021},
url = {https://github.com/TinkerTools/tinker9},
note = {{Washington University in St. Louis}, accessed: T9_ACCESSED}
}`;

const t9_github_ris = `TY  - COMP
TI  - Next Generation of Tinker with GPU Support
AU  - Wang, Zhi
PY  - 2021
Y2  - T9_ACCESSED
ST  - Tinker9
UR  - https://github.com/TinkerTools/tinker9
PB  - Washington University in St. Louis
ER  -
`;

function t9_dl_github_bibtex()
{
   let text = t9_github_bib.replace("T9_ACCESSED", t9_accessed_bibtex());
   let filename = "tinker9_github.bib";
   t9_download(filename, text);
}
function t9_dl_github_ris()
{
   let text = t9_github_ris.replace("T9_ACCESSED", t9_accessed_ris());
   let filename = "tinker9_github.ris";
   t9_download(filename, text);
}

// The Tinker 8 Paper

const t8_paper_bib = `@article {Tinker8_Paper,
title = {{Tinker 8: Software Tools for Molecular Design}},
volume = {14},
issn = {1549-9618},
shorttitle = {{Tinker 8}},
doi = {10.1021/acs.jctc.8b00529},
number = {10},
journal = {Journal of Chemical Theory and Computation},
author = {Rackers, Joshua A. and Wang, Zhi and Lu, Chao and Laury, Marie L. and Lagardère, Louis and Schnieders, Michael J. and Piquemal, Jean-Philip and Ren, Pengyu and Ponder, Jay W.},
month = oct,
year = {2018},
pages = {5273-5289},
}`;

const t8_paper_ris = `TY  - JOUR
T1  - Tinker 8: Software Tools for Molecular Design
A1  - Rackers, Joshua A.
A1  - Wang, Zhi
A1  - Lu, Chao
A1  - Laury, Marie L.
A1  - Lagardère, Louis
A1  - Schnieders, Michael J.
A1  - Piquemal, Jean-Philip
A1  - Ren, Pengyu
A1  - Ponder, Jay W.
JF  - Journal of Chemical Theory and Computation
Y1  - 2018/10/09/
PY  - 2018
DO  - 10.1021/acs.jctc.8b00529
VL  - 14
IS  - 10
SP  - 5273
EP  - 5289
JO  - J. Chem. Theory Comput.
LA  - en
SN  - 1549-9618
ST  - Tinker 8
UR  - https://pubs.acs.org/doi/10.1021/acs.jctc.8b00529
ER  -
`;

function t8_dl_bibtex()
{
   let text = t8_paper_bib;
   let filename = "tinker8_paper.bib";
   t9_download(filename, text);
}
function t8_dl_ris()
{
   let text = t8_paper_ris;
   let filename = "tinker8_paper.ris";
   t9_download(filename, text);
}
