"""PDF Template Maker
"""
## 1 import libraries
from fpdf import FPDF
import pandas as pd

## 2. Store FPDF Object in a variable to operate on.
pdf = FPDF(orientation="portrait", unit="mm", format="A4")

## 3. Store the data from topics.csv file into a dataframe
df = pd.read_csv("Files/topics.csv")

## 16. Set auto page break to false because this was making the footer title go to next page
pdf.set_auto_page_break(False)

## Set a global variable to store the value of the page number
page = 1

## 4. Create a for loop to iterate over the rows in topics.csv
for index, row in df.iterrows():
    ## 5. Create a page with add_page method
    pdf.add_page()

    ## 6. Set font family to times, style to bold, and size to 24
    pdf.set_font(family="Times", style="B", size=24)

    ## 7. Set font color to grey
    pdf.set_text_color(100,100,100)

    ## 8. Create a Header cell with max width, height to 20, aligned to left, with no border
    pdf.cell(w=0, h=20, txt=row["Topic"], align="L", ln=1, border=0)

    ## 9. Create a divider after header with x1 distance from left border to line start, y2 distance from top border to line start, x2 distance from line start to line end, and y2 distance from line end to top border
    pdf.line(10, 25, 200, 25)

    ## 10. Add space using ln method, which represents break line
    pdf.ln(255)

    ## 11. Create a footer divider
    pdf.line(10, 285, 200, 285)

    ## 12. Set pg number font on footer
    pdf.set_font(family="Times", style="B", size=9)

    ## 13. Write page number in bold using page global value and no line break to add footer title in the same line.
    pdf.cell(w=20, h=8, txt=f"{page}", align="L", ln=0, border=0)

    ## increase value of page global variable
    page += 1

    ## 14. Set Footer Title Font
    pdf.set_font(family="Times", size=9)

    ## 15. Write Footer title aligned to right
    pdf.cell(w=0, h=8, txt=row["Topic"], align="R", ln=1, border=0)

    ## 17. Add a nested for loop to add the number of pages mention in topics.csv for each topic. This for loops starts the index at 0 and counts to (excluding the number itself) whatever number is stored in pages column in the row of the topic being iterated in the loop above.
    for i in range(int(row["Pages"])-1):  ## 18. We do -1 since 1 page which includes header is already created above

        ## 19. We repeat the code from the previous loop, without the header, and adjust the line breaks
        pdf.add_page()
        pdf.ln(275)  ## 20. We adjust the line breaks. Since there is no header text, we need to add more line breaks equal to header cell's height
        pdf.line(10, 285, 200, 285)
        pdf.set_font(family="Times", style="B", size=9)
        pdf.cell(w=20, h=8, txt=f"{page}", align="L", ln=0, border=0)
        page += 1
        pdf.set_font(family="Times", size=9)
        pdf.cell(w=0, h=8, txt=row["Topic"], align="R", ln=1, border=0)


pdf.output("PDF Template.pdf")
