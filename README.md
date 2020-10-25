# CheckOn

<p align="center">
<img src="https://user-images.githubusercontent.com/46602793/97069377-e3aa3980-160a-11eb-8766-684923dc14dc.png" width="15%" height="15%">
<img src="https://user-images.githubusercontent.com/46602793/97069291-42bb7e80-160a-11eb-9536-85806bcda6a8.gif">
</p>

<p align="center">
  <a href="https://www.sungshin.ac.kr/sites/main_kor/main.jsp">Website</a>
  ·
  <a href="https://drive.google.com/file/d/1u6kN9E-QRZh2bl-Rcmqq59K7-ks2JAwc/view?usp=sharing">Documentation</a>
</p>  
   
   
   
**"ChckOn 설명할 간단한 문장입니다하하하"**  
- 기능1 : 와아아아아
- 기능2 : 와아아아아
- 기능3 : 와아아아아



***

## On-line Hackathon - LOTTE X LIKE LION 👩‍💻
<p align="center">
<img width="839" alt="해커톤슬로건" src="https://user-images.githubusercontent.com/46602793/96824481-e6b9f400-1469-11eb-8438-06d3f5f282b9.png" width="30%">
</p>

### 주제
롯데의 유통, 물류, 제조 서비스 중에서 현재 불편함을 느끼는 부분을 스스로 도출하거나, 롯데그룹에 새롭게 제안하고 싶은 주제를 자유롭게 개발하는 방향

### 팀원
🔮**LikeLion 8th Members - Sungshin Women's University**🦁  

| 이름 | 담당 |
| --- | --- |
| 김지수([Kim-jisoo11](https://github.com/Kim-jisoo11)) | 백엔드&프론트엔드, UX/UI |
| 김지우([jiuuucy](https://github.com/jiuuucy)) | 백엔드&프론트엔드, UX/UI |
| 도수빈([svdoit](https://github.com/svdoit)) | 백엔드&프론트엔드 |
| 이성민([icechocola05](https://github.com/icechocola05)) | 백엔드&프론트엔드 |

***

## 프로젝트 소개
### 1. 프로젝트 기획 의도

### 2. 주요 기능

#### 2.1 메인 페이지  
<img src="https://user-images.githubusercontent.com/46602793/97104800-f51e3f00-16f9-11eb-82b1-b87e9fa45b5f.gif">  

설명


#### 2.2 로그인 페이지

설명

<img alt="로그인페이지" src="https://user-images.githubusercontent.com/46602793/97105128-18e28480-16fc-11eb-8971-641b34f08b15.png" width="600">


#### 2.3 쇼핑 페이지

설명

<img alt="쇼핑페이지" src="https://user-images.githubusercontent.com/46602793/97105127-17b15780-16fc-11eb-9930-f33b615a511f.png" width="600">


#### 2.4 장바구니 페이지

설명



  
    def cart(request):
      categories = Category.objects.all()
      cart = Cart.objects.filter(user=request.user)
      paginator = Paginator(cart, 10)
      page = request.GET.get('page')
      posts = paginator.get_page(page)
      total_prices = 0
      for i in cart:
          i.products.price = i.products.price * i.quantity
          total_prices = total_prices + i.products.price    
      cart.totalAmount = total_prices

    # 카테고리별 산 상품 종류 합계
    isBought = {}
    for i in cart:
        if i.category_id in isBought:
            sum = isBought.get(i.category_id) + 1
            isBought[i.category_id] = sum
        else:
            isBought[i.category_id] = 1

    # 구매 제품 종류 합계
    totalSum=0
    for key, value in isBought.items():
        totalSum = totalSum + value
    

    # 카테고리 통계
    countProduct = {}
    context = {'cart': cart, 'categories': categories, 'posts' : posts, 'totalSum' : totalSum}
    for i in cart:
        countProduct[i.category_id] = isBought.get(i.category_id) / totalSum * 100

    for key, value in countProduct.items():
        context = {'cart': cart, 'categories': categories, 'posts' : posts, 'countProduct' : countProduct, 'totalSum' : totalSum}

    return render(request, 'cart.html', context)


### 3. 



