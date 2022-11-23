# agrograde_task
Day 1:
As i have not worked on image segmentation,i looked for the process to segment the objects.
Thought of simply applying threshold to the image(as the onion image seems to be on a black background)
It didnt work as,the black background was actually not actually black(had some noise)
So,i had few options:
1.Use a custom threshold and filter the onion
2.Use k means and other unsupervised learning algorithms
3.Use grab cut algorithm of opencv
4.Let the algorithm choose the threshold

I chose option 1 as simple method initially.
20 threshold value seemed to work perfectly on the greyscale converted image.
I used this image mask to segment the image and used bitwiseand to mask the image.

Now, subtracted the number of pixels with value 255 with the total number of pixels and found the percentage.
Thus,i was able to find the percentage of total pixel area covered by the onion.

Issues faced:
I was facing some issues masking rgb image with greyscale mask image(Fixed)

Tasks done:
1.Segmented the onion from the image successfully

Task to be done:
I tried to find the perimeter of the image by finding the contour.
There is some issue with the contour calculation which needs to be addressed.

I have attached the code and screenshot of work done on day 1
