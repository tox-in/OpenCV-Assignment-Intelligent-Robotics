import cv2
from pyzbar.pyzbar import decode
import numpy as np
import zxing

reader = zxing.BarCodeReader()
image_path = "image05.png" 
image = cv2.imread(image_path)

decoded = reader.decode(image_path)

if decoded:
    print(f"Decoded Data: {decoded.parsed}")
    print(f"Barcode Format: {decoded.format}")

    if hasattr(decoded, "points") and decoded.points:
        try:
            points = np.array(decoded.points, dtype=np.int32).reshape((-1, 1, 2))
            cv2.polylines(image, [points], isClosed=True, color=(0, 255, 0), thickness=2)

            x, y = points[0][0]
            cv2.putText(image, decoded.parsed, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
        except Exception as e:
            print(f"Error processing bounding box: {e}")
  
    cv2.imshow("Aztec Code with Annotation", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
   
    output_file = "decoded_aztec.png"
    cv2.imwrite(output_file, image)
    print(f"Annotated image saved as {output_file}")
else:
    print("Failed to decode the Aztec code.")