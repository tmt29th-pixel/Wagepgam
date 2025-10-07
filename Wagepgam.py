dic = {
    "username": "ali",
    "pass": "1234567",
    "name": "Ali Ahmed",
    "age": 21,
    "mail": "ali@mail.ru",
    "height": "176 سم",
    "phone": "+964 771 234 567",
}
max_attempts = 3
attempts = 0
while attempts < max_attempts:
    username_input = input("أدخل اسم المستخدم: ").strip().lower()
    password_input = input("أدخل كلمة السر: ").strip().lower()
    if not username_input or not password_input:
        print("يرجى إدخال اسم مستخدم وكلمة سر صحيحين (لا تترك فارغًا)!")
        continue
    if username_input == dic["username"].lower() and password_input == dic["pass"].lower():
        print(f"مرحباً {dic['name']}")
        print(f"عمرك هو {dic['age']}")
        print(f"بريدك الإلكتروني هو {dic['mail']}")
        print(f"طولك هو {dic['height']}")
        print(f"رقم هاتفك هو {dic['phone']}")
        break 
    else:
        attempts += 1
        remaining = max_attempts - attempts
        
        if remaining > 0:
            print(f"> اسم المستخدم أو كلمة السر خاطئة - ({remaining} محاولات متبقية)")
        else:
            print("تم قفل الحساب!")
            dic.clear()
            break
if attempts >= max_attempts and "username" not in dic:
    print("تم رفض الوصول. جرب مرة أخرى لاحقًا.")
