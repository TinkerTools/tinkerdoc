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
   return `${t9_accessed_year}/${t9_accessed_month_num}/${t9_accessed_date}`;
}

//----------------------------------------------------------------------//

// Tinker9 on GitHub: bib

const t9_github_bib = `@misc {Tinker9_GitHub,
author = {Wang, Zhi and Ponder, Jay W.},
title = {{Tinker9: Next Generation of Tinker with GPU Support}},
shorttitle = {{Tinker9}},
year = {2021},
url = {https://github.com/TinkerTools/tinker9},
note = {accessed: T9_ACCESSED}
}`;

const t9_github_ris = `TY  - ELEC
TI  - Next Generation of Tinker with GPU Support
AU  - Wang, Zhi
AU  - Ponder, Jay W.
DA  - 2021///
PY  - 2021
Y2  - T9_ACCESSED
ST  - Tinker9
UR  - https://github.com/TinkerTools/tinker9
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
