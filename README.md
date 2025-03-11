# Projected Area Calculation for Microalgae using Three-Dimensional Models

## Authors
Borics Gábor<sup>1</sup>, Verona Lerf<sup>1,2</sup>, János Falucskai<sup>3</sup>, Viktória B-Béres<sup>1</sup>, Tibor Kisantal<sup>1</sup>, István Tóth<sup>1</sup>, Enikő-T-Krasznai<sup>1</sup>, Igor Stanković<sup>4</sup>, Judith Görgényi<sup>1</sup>, Áron Lukács<sup>1,5</sup> & Gábor Várbíró<sup>1</sup>

## Affiliations
1. HUN-REN Centre for Ecological Research, Institute of Aquatic Ecology, Functional Algology Research Group, Bem square 18/c, H-4026 Debrecen, Hungary  
2. University of Debrecen, Juhász-Nagy Pál Doctoral School of Biology and Environmental Sciences, Egyetem sqr. 1. H-4032 Debrecen, Hungary  
3. University of Nyíregyháza, Institute of Mathematics and Informatics, Sóstói str 31/B, Nyíregyháza, HU-4400 Nyíregyháza, Hungary  
4. Josip Juraj Strossmayer Water Institute, Ulica grada Vukovara 220, HR-10000 Zagreb, Croatia  
5. University of Helsinki, Lammi Biological Station, Pääjärventie 320, 16900 Lammi, Finland  

## Abstract
Projected (shaded) area (Ā) is a crucial morphological trait of microalgae, influencing light acquisition and sinking properties. However, species-specific Ā values are currently unavailable. Although Ā can be analytically calculated for convex shapes using surface area data, such data are missing from microalgae databases. Additionally, no established method exists for calculating the projected area of concave shapes.

This study proposes a probabilistic numerical approach and computer simulation to determine Ā for all 3D objects. We created shape-realistic 3D models of over 800 microalgae and placed them in a virtual space. Utilizing a virtual orthogonal camera system and a probabilistic optimization framework, we measured and calculated their projected areas. Our approach was validated against convex shapes using the analytical Ā = surface area/4 formula, achieving an estimation bias of less than 5%.

We demonstrated that morphological differences among species can result in up to sixfold variations in Ā for the same volume. We further analyzed how Ā values correlate with previously proposed morphological metrics (e.g., compactness, relative surface area extension, relative elongation, Gald/width ratio, surface area constant, volume constant). While the applied models explained a significant portion of the variance, the large scatter prevents accurate estimates for Ā.

We identified spindle-form, filamentous, and loosely packed coenobial colonies as the most effective adaptations for maximizing Ā. This study presents an innovative methodology and a dataset containing Ā values for 844 planktic freshwater microalgae. Though limited to species from the Pannonian and Dinaric ecoregions, the dataset is applicable to other regions due to the cosmopolitan nature of planktic algae. Our findings enhance the understanding of phytoplankton functionality and contribute to improved predictive models for their compositional changes.

## Corresponding Author
Gábor Várbíró - [Email: varbirog@gmail.com](mailto:varbirog@gmail.com)

---

## How to Cite
If you use this dataset or methodology, please cite our : XXXXXXXXXXXXXXXXXX
DOI : XXXXXXXXXXXXXXXXXXXXXXXXXXXX

#  File description 

## 📁 Directory Structure

- **`data/`** - Contains raw and processed data files.  
- **`scripts/`** - Includes analysis scripts for data processing and visualization.  
  - `process_data.py` - Cleans and formats the raw data for analysis.  
  - `analysis.R` - Performs exploratory data analysis and generates visualizations.  
  - `shiny_app.R` - Shiny application for interactive data exploration.  
- **`results/`** - Stores output figures, tables, and reports.  
  - `figures/` - Contains plots and graphs generated from analysis.
  - 'ESM/' -   Contains plots and
  - `tables/` - Stores tabular results in CSV/Excel format.  
- **`requirements.txt`** - Lists required Python packages for reproducibility.  


## COPYRIGHT

This package is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or any later version.

Note: only part of the files distributed in the package belong to the SOM Toolbox. The package also contains contributed files, which may have their own copyright notices. If not, the GNU General Public License holds for them, too, but so that the author(s) of the file have the Copyright.

This package is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this package (file COPYING); if not, write to the Free Software Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
## LICENSING THE LIBRARY FOR PROPRIETARY PROGRAMS
As stated in the GNU General Public License (see the license in COPYING) it is not possible to include this software library in a commercial proprietary program without written permission from the owners of the copyright.
