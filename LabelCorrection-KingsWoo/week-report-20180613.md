# 周报20180613

---

## 疾病筛选

### 1. 糖尿病

	select tijianbm
	from TJGLTEST.TJ_GERENZJZD t
	where zhenduanxx like '%糖尿病%'
	    and not (zhenduanxx like '%糖尿病？%'
		    or   zhenduanxx like '%糖尿病?%'
		    or   zhenduanxx like '%糖尿病史%'
		    or   zhenduanxx like '%糖尿病病史%'
		    or   zhenduanxx like '%早期%'
		    or   zhenduanxx like '%待%'
		    or   zhenduanxx like '%可疑%'
		    or   zhenduanxx like '%视网膜%'
		    or   zhenduanxx like '%肾病%'  
		    or   zhenduanxx like '%可能%'
		)

	  
### 2. 肥胖

	select tijianbm
	from TJGLTEST.TJ_GERENZJZD t
	where zhenduanxx like '%肥胖%'
	   or zhenduanxx like '%超重%'
	   
### 3. 高血糖
	
 	select tijianbm
	from TJGLTEST.TJ_GERENZJZD t
	where zhenduanbm in (005703, 409302)
		or (
		  zhenduanxx like '%糖尿病%'
	      and not (zhenduanxx like '%糖尿病？%'
		      or   zhenduanxx like '%糖尿病?%'
			  or   zhenduanxx like '%糖尿病史%'
			  or   zhenduanxx like '%糖尿病病史%'
			  or   zhenduanxx like '%早期%'
			  or   zhenduanxx like '%待%'
			  or   zhenduanxx like '%可疑%'
			  or   zhenduanxx like '%视网膜%'
			  or   zhenduanxx like '%肾病%'  
			  or   zhenduanxx like '%可能%'
		  )
		)

### 4. 高血压

	select tijianbm
	from TJGLTEST.TJ_GERENZJZD t
	where (zhenduanbm in (407113,006435,407056,000709) and not zhenduanxx like '%轻度%')
	   or (zhenduanbm in (407395) and not zhenduanxx like '%高血压病史%')
	
### 5. 脂肪肝

	select tijianbm
	from TJGLTEST.TJ_GERENZJZD t
	where zhenduanxx like '%脂肪肝%'
	  and not (zhenduanxx like '%倾向%'
		   or  zhenduanxx like '%脂肪肝考虑%'
		   or  zhenduanxx like '%?%'
		   or  zhenduanxx like '%？%'   
	  )   
	  
### 6. 肝功能异常

	select tijianbm
	from TJGLTEST.TJ_GERENZJZD t
	where zhenduanxx like '%肝功能%'
	  and not (zhenduanxx like '%待查%')
	  
	  
### 7. 肾功能异常

	select tijianbm
	from TJGLTEST.TJ_GERENZJZD t
	where zhenduanxx like '%肾功能%'
	
### 8. 高脂血症

	select tijianbm
	from TJGLTEST.TJ_GERENZJZD t
	where zhenduanxx like '%高脂%'
	  and not (zhenduanxx like '%史%')

	  
### 9. 高尿酸血症

	select tijianbm
	from TJGLTEST.TJ_GERENZJZD t
	where zhenduanxx like '%高尿酸血症%'
	
### 10. 胆囊炎

	select tijianbm
	from TJGLTEST.TJ_GERENZJZD t
	where zhenduanxx like '%胆囊炎%'