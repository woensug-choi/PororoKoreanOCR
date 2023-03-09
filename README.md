<h2 align="center">
Korean OCR using pororo (Mod. by Woensug Choi)
</h2>

This is a Korean OCR Python code using the Pororo library.
Based on https://github.com/yunwoong7/korean_ocr_using_pororo

## Modification

- Added `dilatation_factor` to expand the recognizing area 
  - 선택지 인식이 안되는 부분을 해결하기 위해 도입
  - `quickstart.py` 참조

<div align="center">
  <img src="https://img.shields.io/badge/python-v3.10.6-blue.svg"/>
  <img src="https://img.shields.io/badge/torch-v1.13.1-blue.svg"/>
  <img src="https://img.shields.io/badge/torchvision-v0.14.1-blue.svg"/>
  <img src="https://img.shields.io/badge/opencv_python-v4.7.0.72-blue.svg"/>
</div>

## Requirements

- torch
- torchvision
- opencv-python

You can install it from PyPI:

```sh
pip install torch
pip install torchvision
pip install opencv-python
```

## PORORO: Platform Of neuRal mOdels for natuRal language prOcessing

[pororo](https://github.com/kakaobrain/pororo) is a library developed by KakaoBrain for performing natural language processing and speech-related tasks. 

This repository is configured to only include the OCR functionality from the pororo library. If you wish to use other pororo features such as natural language processing, please install pororo through `pip install pororo`.

## Usage

```python
from pororo import Pororo

ocr = PororoOcr()
image_path = input("Enter image path: ")
text = ocr.run_ocr(image_path, debug=True)
print('Result :', text)
```

------

<div align="center">
<img src="https://user-images.githubusercontent.com/7955120/224110625-75458f26-14c3-49f7-b79a-ce3867f71fc7.jpg" width="50%">
</div>

24, 다음 글의 제목으로 가장 적절한 것은? The recent "cycling as a lifestyle" crase has expressed itsefi in an increase in the number of active cyclists and in growth di cyrcling club menberstip in several Buropean, American, Australian and Asian urtan areas. It has also been acompanied) ky a symbolic reinterpretation of the bicycle, After the bicyce had been asociated with poverty for many years, expensive rereastional bicycles or recreationally-inspired commating hicycles have suddenly become aspirational products in artan eovinmments, In present times, cycling has become an activity which is also pertormed for its demonstrative value, its role in jidenity constroction and its effectiveness in impressing obers and signaling social status. To a certain extet, cycing has tumed inmo a symbolic marker of the well-dft. Ohvioasy. vabse-laden consumption bebavior is by no mesms limited to cycling, However, the link with identity costruction and) cmspiruous cnsumption has become particularly manifest in the case of cycling. * comspicuous: 눈에 잘 띄는 Cyctling Contributes to a City's Anmosphere and lidemtity The Rise of Cycling; A New Status Symbol of City Dwellers Cycting Is Weath-Building but Worsens Social Inequality HHow to Encourage and Sustain the Bicycle Crape in Uinban Areas, Espanding Hike Lane Networks Can Lead to More Inclusive Cbies