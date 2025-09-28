# Universal Quantum Mesh Equation (WME)

## 📄 Publications & Preprints

•⁠  ⁠[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17216874.svg)](https://doi.org/10.5281/zenodo.17216874) *Finite-Time Closure Theorem and Minimal-Energy Mesh Framework*

•⁠  ⁠[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17216258.svg)](https://doi.org/10.5281/zenodo.17216258) *Mass-Driven Time and the Theorem of Entropic Closure*

•⁠  ⁠[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17186773.svg)](https://doi.org/10.5281/zenodo.17186773) *WME System – Plasma Threshold and Energy Partition*

•⁠  ⁠[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17186420.svg)](https://doi.org/10.5281/zenodo.17186420) *Orbital Inspiral and Minimal Dissipation Models*

•⁠  ⁠[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17181035.svg)](https://doi.org/10.5281/zenodo.17181035) *Energy-Efficient AI via Universal Quantum Mesh Equation*

•⁠  ⁠[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17180764.svg)](https://doi.org/10.5281/zenodo.17180764) *Universal Quantum Mesh Equation – Foundational Theorem*

This repository contains toy models for the *Universal Quantum Mesh Equation (WME)*, demonstrating its applications across metals, AI, and black holes.  
All models are *reproducible in 1 minute*.

--- WME Toy Models — Run in 1 Minute

Três scripts **reproduzíveis** que demonstram, de forma simples e rápida, as ideias centrais:
1. **Metal (curvatura ≠ 0)** — não há trajetória linear global: tendências de **escape** ou **decay** emergem.
2. **IA (fechamento de potência)** — iteração multiplicativa com λ < 1 converge para **zero** (fechamento); com λ > 1 tende ao **escape**.
3. **Buraco negro (tempo próprio finito)** — decaimento **m'(τ) = -k·m^p, p>1** leva a extinção em **tempo finito**.

> **Reprodução ultrarrápida**: requer Python 3.10+; `matplotlib` é opcional (apenas para salvar gráficos).

## Como rodar (1 minuto)

```bash
# 1) Metal (sem plot)
python metal_toy.py --steps 300 --alpha 0.08 --beta 0.6 --gamma 0.02 --plot 0

# 2) IA (fechamento; lam < 1)
python ai_toy.py --lam 0.98 --steps 500 --x0 1.0 --plot 0

#    Escape (lam > 1)
python ai_toy.py --lam 1.02 --steps 200 --x0 0.2 --plot 0

# 3) Buraco negro (p>1 => tempo finito)
python blackhole_toy.py --m0 1.0 --k 0.8 --p 1.5 --dt 0.001 --plot 0
```

Para salvar gráficos (`*.png`), adicione `--plot 1` aos comandos.

## Estrutura do repositório (sugerida)

```
wme-toys/
  ├─ metal_toy.py
  ├─ ai_toy.py
  ├─ blackhole_toy.py
  ├─ README.md
  ├─ requirements.txt
  ├─ LICENSE
  └─ CITATION.cff
```

## Cite como (DOIs Zenodo)

Use os seus quatro DOIs públicos do CERN Zenodo aqui (edite abaixo):
- **DOI 1 (WME – Metal):** `10.5281/zenodo.xxxxxxx`
- **DOI 2 (WME – IA):** `10.5281/zenodo.xxxxxxx`
- **DOI 3 (WME – Buraco Negro):** `10.5281/zenodo.xxxxxxx`
- **DOI 4 (WME – Teorema Matemático):** `10.5281/zenodo.xxxxxxx`

> Dica: após adicionar os DOIs, você pode incluir o badge do Zenodo na primeira linha do README. Exemplo (troque o número pelo seu):  
> `![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.xxxxxxx.svg)`

## Como publicar no GitHub (passo a passo)

```bash
# 1) criar pasta e iniciar repositório
mkdir wme-toys && cd wme-toys
# (copie para cá os arquivos deste pacote: *.py, README.md, requirements.txt, LICENSE, CITATION.cff)

git init
git add .
git commit -m "WME toy models: metal, AI, black hole (run in 1 minute)"

# 2) criar repositório no GitHub (via web) e copiar a URL SSH/HTTPS
git branch -M main
git remote add origin https://github.com/<seu-usuario>/wme-toys.git
git push -u origin main
```

## Requisitos

- Python 3.10+
- (Opcional) `matplotlib` para salvar gráficos: `pip install -r requirements.txt`

## Licença
Este repositório usa a licença **MIT** (veja `LICENSE`).

