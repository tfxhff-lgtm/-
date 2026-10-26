# Sol y Mesa — แพ็กเกจ GitHub Pages

ไฟล์ `index.html` เป็นเว็บไซต์หน้าเดียวที่สลับดูได้ 5 หน้า ภาพถ่ายถูกฝังไว้ในไฟล์แล้ว จึงไม่ต้องอัปโหลดโฟลเดอร์ภาพหรือ dependencies เพิ่ม

## วิธีเปิดเป็นเว็บไซต์บน GitHub Pages

1. แตก ZIP แล้วอัปโหลด `index.html` ไปไว้ที่ **โฟลเดอร์ราก** ของ Repository จากนั้น Commit ไฟล์
2. เปิด Repository บน GitHub แล้วไปที่ **Settings → Pages**
3. ใน **Build and deployment** เลือก **Deploy from a branch**
4. เลือก branch ที่ใช้ (เช่น `main`) และโฟลเดอร์ `/(root)` แล้วกด **Save**
5. รอการ Deploy แล้วเปิด URL ที่ GitHub แสดงในหน้า Pages

การเปิดไฟล์ `.html` ใน Code view ของ GitHub จะแสดงซอร์สโค้ด ไม่ใช่หน้าเว็บ ต้องใช้ GitHub Pages เพื่อแสดงเป็นเว็บไซต์ GitHub Pages อาจใช้เวลาหลายนาทีกว่าการ Deploy จะเสร็จ

**คำเตือน:** เว็บไซต์ที่เผยแพร่ด้วย GitHub Pages จะเข้าถึงได้สาธารณะบนอินเทอร์เน็ต แม้ Repository จะเป็น private ในบางแผนหรือการตั้งค่าองค์กร อย่าใส่ข้อมูลลับก่อนเปิดเผยแพร่

## เอกสาร GitHub

- [กำหนดแหล่งที่มาสำหรับเผยแพร่ GitHub Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site)
- [เริ่มต้นใช้งาน GitHub Pages](https://docs.github.com/pages/quickstart)
