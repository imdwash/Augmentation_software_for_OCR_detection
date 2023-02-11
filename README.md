
# Augmentation Software for OCR detection

This software is designed to support OCR (Optical Character Recognition) model development by providing the necessary tools to augment the detection dataset. With the growing demand for high accuracy in OCR technology, it is essential to have a robust dataset that can capture a wide variety of scenarios and variations in text characters. This software helps in collecting and labeling the data to create a well-rounded dataset, enabling OCR models to be trained on a diverse set of images and improve the overall accuracy of the model. Whether you're working on a research project, developing a new OCR product, or enhancing existing OCR technology, this software is an indispensable tool for augmenting the detection dataset of your OCR models.

## Deployment

To deploy this project

```bash
  run 'MainSoftware.py'
```

## Description

![Home Screen!](Screenshots/Capture.JPG)

This home screen where user can either choose to view images or augment images

![Augmentation Screen!](Screenshots/Capture2.JPG)

Various Augmenation methods can be selected

![Rotation!](Screenshots/Capture3.JPG)

Rotation Operation

![Blurring!](Screenshots/Capture4.JPG)

Blurring Operation

![Rotation Output!](Screenshots/Capture5.JPG)

This is output of rotation operation 

- Select 'Augmentation' box
- Select folder containing images, images most have bounding box with same name in the ICDAR format

![Show!](Screenshots/Capture7.JPG)

Note: 
- end words like '*MRP NPR.Rs.30/-' are optional
- For converting paddleocr label i.e. 

![Conversion!](Screenshots/Capture6.JPG)

you can run 'ppOcr2BB.py'

```bash
  run python ppOcr2BB.py --pp_txt=location of ppocr label.txt --out_dir= directory where you want to keep .txt files
```
eg,

python ppOcr2BB.py --pp_txt=C:/predicts_db.txt --out_dir=C:/det_db/outtxt/

- Click on the augmentation methods 

- Click on the dropdown menu in the bottom to generate number of images

- Click 'Generate' to generate images, images will be saved in the folder named 'Augmentation' in the same folder where images are located.

For Viewing images,

- Click on 'open directory'
- Click 'open select' to view one image at a time
- Click 'Open all' to view all images, to view next - - click 'd', to go back click 'a' , to close the image click 'q'



## If this repository helps you，please star it. Thanks.
