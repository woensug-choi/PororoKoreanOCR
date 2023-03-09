import time
start_time = time.time()

from PororoOcrWrapper import PororoOcr
ocr = PororoOcr(dilatation_factor=2.0) # dilatation_factor 받도록 수정함
# ocr.get_available_langs()

# Starting up time check
import_time = time.time() - start_time
print(import_time)

ocr.run_ocr('assets/images/test5.jpg', dilatation_factor=4)
print(ocr.get_ocr_result()['description'][0])