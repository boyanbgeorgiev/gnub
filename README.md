# SeaLifeScan ReadMe


#  Въведение 
Голяма част от хората не са запознати с разнообразието на морския свят, до който се докосват, когато посещават морското крайбрежие. Затова решихме да създадем Web-приложение, което да решава този проблем.
SeaLifeScan има за цел да изгради система за автоматично разпознаване на морски видове -акули от изображение. Тази система ще бъде способна да анализира изображения, предоставени от потребителя, и да идентифицира различните морски видове, които са представени на тях. 

#  Функционаност
Това, което прави нашият уебсайт уникален, е категоризирането на съответното животно по животински вид. След идентификацията предоставяме подробни данни свързани с сниманото от него животно. Организирали сме код по начин, който дава възможност за въвеждане на нови dataset-ове бързо и лесно, което позволява постигането на по-точен и моделируем изкуствен интелект като подготовка за въвеждане на други животински видове.


# Архитектура 
1.Frontend
	UI:
 	За изграждането на нашия сайт използвахме HTML и библиотеката tailwind на CSS. Избрахме тази библиотека, защото дава възможност за по-лесна моделируемост и осигурява готови безплатни елементи за по-лесно изграждане на UI. Улеснява писането на сайта заради 	удобните, функционални класове, които предоставя библиотеката.
  	JS: 
	JavaScript предлага динамична обработка на събития в уебстраниците, позволява на потребителите да качват файлове, да ги обработват и да виждат резултатите, без да се презарежда страницата. JavaScript кодът осигурява функционалност за качване на файл, преглед на 	неговото съдържание, изпращане на съдържанието към сървъра за обработка и визуализиране на получения резултат на HTML страницата.

2.Backend
	Flask:
	Използвахме framework-a Flask, защото предлага лесен начин за изграждане на Web-приложения и връзка  АPI. Чрез файла main.py изображението се изпраща към AI-a, качено от потребителя, във формат base 64.
	AI:
 	След неуспешни опити без готов CNN и с ResNet50, решихме, че най-удобен за нас е MobileNetV2. Той е най-ефикасен от масивните CNN-ове. Т.е. с наличното време и хардуер това е най-добрият вариант за train-ване за нашите цели. 

# Бъдещи Имплементации
 Идеите ни за в бъдеще обхващат повече морски видове, както и информация за тях. Проектът има потенциал да се разрастне с повече dataset-ове, както и да добави нови функционалности като например: локация на снимката, за да проверява дали организмът е в натуралния	си хабитат и проверка дали е застрашен от изчезване.

# Технологии
	
- CSS Tailwind - Уебсайт Дизайн
- JS - Image upload system
- Python Tensorflow and MobileNetV2 - CNN training
- Python Flask - Local Server and Connection between Frontend and API
- Json - Configures npm and Development Environment.
# Инсталация
- Python библиотеки
  
		pip install -r requirements.txt

# Отбор GNUB
- Георги Пъстраков 8В
- Невена Димитрова 8Б
- Никола Колев 8А
- Юлиян Цончев 8А
- Боян Георгиев 8А

