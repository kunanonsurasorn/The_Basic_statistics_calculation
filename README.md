# The_Basic_statistics_calculation
โปรเจคนี้จัดทำขึ้นเพื่อพัฒนาโปรแกรมการคำนวณทางสถิติเบื้องต้นสำหรับชุดข้อมูลในรูปแบบ CSV ที่มีช้อมูลเป็นจำนวนมาก การใช้โปรแกรมนี้จะช่วยให้ผู้ใช้สามารถทราบข้อมูลทางสถิติเบื้องต้นของข้อมูลที่ผู้ใช้สนในใจเช่น ค่าต่ำสุด ค่ามัธยฐาน ค่าเฉลี่ย ค่าสูงสุด พิสัย ค่าเบี่ยงเบนมาตรฐาน ค่าควอร์ไทล์ และ จำนวนข้อมูล

![project_gui1](https://github.com/kunanonsurasorn/The_Basic_statistics_calculation/blob/main/project_gui1.jpg)

![project_gui2](https://github.com/kunanonsurasorn/The_Basic_statistics_calculation/blob/main/project_gui2.jpg)

## 1. Library ที่ใช้ในการพัฒนา

    1.1 Tkinter

    1.2 Pandas

## 2. สถิติที่ใช้ในการคำนวณ

    2.1 ค่าต่ำสุด
        min()
        
    2.2 ค่ามัธยฐาน
        median()
        
    2.3 ค่าเฉลี่ย
        mean()
        
    2.4 ค่าสูงสุด
        max()
        
    2.5 ค่าพิสัย
        y.max()-y.min()
        
    2.6 ค่าเบี่ยงเบนมาตรฐาน  
        std()
        
    2.7 ค่าควอร์ไทล์
        quantile(0.25) สำหรับควอร์ไทล์ที่ 1
        quantile(0.50) สำหรับควอร์ไทล์ที่ 2
        quantile(0.75) สำหรับควอร์ไทล์ที่ 3
        
    2.8 จำนวนข้อมูล
        count()

## 3. ข้อเสนอแนะ

    โปรเจคนี้สามารถนำ matplotlib มาใช้สำหรับการดูความสัมพันธ์ระหว่างตัวแปร x และ ตัวแปร y ในรูปแบบกราฟ

## 4. ที่มาของชุดข้อมูล

    4.1 เว็บไซต์ด้านสถิติประเทศเกาหลีใต้ 
            https://kosis.kr/eng/
    
    4.2 เว็บไซต์ด้านสถิติประเทศสวีเดน 
            https://www.scb.se/en/

![project_gui3](https://github.com/kunanonsurasorn/The_Basic_statistics_calculation/blob/main/project_gui3.jpg)

![project_gui4](https://github.com/kunanonsurasorn/The_Basic_statistics_calculation/blob/main/project_gui4.jpg)

![project_gui5](https://github.com/kunanonsurasorn/The_Basic_statistics_calculation/blob/main/project_gui5.jpg)
  
