# VarDocent - Comprehensive Variant Analysis Pipeline

A modular pipeline for variant filtering, analysis, and format conversion.

## Features
- Universal VCF processing from any variant caller
- Structural variant detection with Delly
- Advanced quality filtering
- Population genetics format conversion
- HWE-based filtering
- Multi-format output support

## Installation
```bash
git clone https://github.com/ankush290307/VarDocent.git
cd VarDocent

# Install dependencies
conda env create -f requirements.txt
conda activate vardocent
