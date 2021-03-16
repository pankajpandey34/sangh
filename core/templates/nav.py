{% load static %}
<nav class="navbar navbar-expand-lg navbar-light style{background-color: :{% url 'undercons' %}f75e16}">
    <a class="navbar-brand" href="{% url 'home' %}"><i class="fas fa-home"></i></a>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="{% url 'undercons' %}navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
    </button>

    <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav mr-auto">
        <li class="nav-item active">
            <a class="nav-link" href="{% url 'undercons' %}">मिशन <span class="sr-only">(current)</span></a>
        </li>
        
            <li class="nav-item">
            <a class="nav-link" href="{% url 'undercons' %}"></a>
        </li>
        <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="{% url 'undercons' %}" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
            शासन के पत्र
            </a>
            <div class="dropdown-menu" aria-labelledby="navbarDropdown">
            <a class="dropdown-item" href="{% url 'dfoletter' %}">वनमंडल के पत्र</a>
            <div class="dropdown-divider"></div>
            <a class="dropdown-item" href="{% url 'ccfletter' %}">मुख्‍य वन संरक्षक के पत्र</a>
            <div class="dropdown-divider"></div>
            <a class="dropdown-item" href="{% url 'pccfletter' %}">प्रधान मुख्‍य वनसंरक्षक के पत्र</a>
            </div>
        </li>
        <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="{% url 'undercons' %}" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
            डाउनलोड
            </a>
            <div class="dropdown-menu" aria-labelledby="navbarDropdown">
            <a class="dropdown-item" target="_blank" href="{% static '/download/RTI.pdf' %}">सूचना का अधिकार अधिनियम</a>
            <div class="dropdown-divider"></div>
            <a class="dropdown-item" href="{% url 'undercons' %}">अधिनियम</a>
            <div class="dropdown-divider"></div>
            <a class="dropdown-item" href="{% url 'undercons' %}">नियम</a>
            <div class="dropdown-divider"></div>
            <a class="dropdown-item" href="{% url 'prapatra' %}">प्रपत्र</a>
            <div class="dropdown-divider"></div>
            <a class="dropdown-item" href="{% url 'rajpatra' %}">राजपत्र</a> 
            <div class="dropdown-divider"></div>
            <a class="dropdown-item" href="{% url 'undercons' %}">सेवा भर्ती नियम</a>                            
            </div>
        </li>
        <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="{% url 'undercons' %}" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
            संघ के पत्र
            </a>
            <div class="dropdown-menu" aria-labelledby="navbarDropdown">
            <a class="dropdown-item" href="{% url 'bhopalsanghletter' %}">वन कर्मचारी संघ भोपाल के पत्र</a>
            <div class="dropdown-divider"></div>
            <a class="dropdown-item" href="{% url 'hardasanghletter' %}">वन कर्मचारी संघ हरदा के पत्र</a>
            </div>
        </li>
        <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="{% url 'undercons' %}" id="navbarDropdown" data-toggle="dropdown">
            अन्‍य आवश्‍यक</a>
            <div class="dropdown-menu mega-menu" aria-labelledby="navbarDropdewn">
                <div class="row">
                    <div class="col-md-4">
                        
                        <a class="dropdown-item" href="{% url 'calcform' %}">ग्रेच्‍युटी का आंकलन</a>
                        <div class="dropdown-divider"></div>
                        <a class="dropdown-item" href="{% url '5680' %}">नियुक्ति दिनांक से वेतनमान</a>
                        <div class="dropdown-divider"></div>
                        <a class="dropdown-item" href="{% url 'undercons' %}">GPS कन्‍वर्टर</a>
                    </div>
                    <div class="col-md-4">
                        <a class="dropdown-item" href="{% url 'fanc' %}">फेंसिग सामग्री केल्‍कुलेशन</a>
                        <div class="dropdown-divider"></div>
                        <a class="dropdown-item" href="{% url 'gurthwise' %}">गोलाईवार वृक्ष गोशवारा</a>
                        <div class="dropdown-divider"></div>
                        <a class="dropdown-item" href="{% url 'undercons' %}">पुनरूत्‍पादन सर्वेक्षण का निर्धारण</a>
                    </div>
                    <div class="col-md-4">
                        <a class="dropdown-item" href="{% url 'undercons' %}">बैंक चालान</a>
                        <div class="dropdown-divider"></div>
                        <a class="dropdown-item" href="{% url 'undercons' %}">कन्‍वर्टर</a>
                        <div class="dropdown-divider"></div>
                        <a class="dropdown-item" href="{% url 'undercons' %}">इन्‍कम टेक्‍स गणना</a>
                        <div class="dropdown-divider"></div>
                        <a class="dropdown-item" href="{% url 'undercons' %}">अन्‍य</a>
                    </div>                                    
                    
                </div>
                
            </div>                            
        </li>
        <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="{% url 'undercons' %}" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
            पदक्रम सूची
            </a>
            <div class="dropdown-menu" aria-labelledby="navbarDropdown">
            <a class="dropdown-item" href="{% url 'rankfg' %}">वनरक्षक</a>
            <div class="dropdown-divider"></div>
            <a class="dropdown-item" href="{% url 'rankforester' %}">वनपाल</a>
            <div class="dropdown-divider"></div>
            <a class="dropdown-item" href="{% url 'rankaro' %}">उपवनक्षेत्रपाल</a>
            </div>
        </li>
        <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="{% url 'undercons' %}" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
            एडमिन
            </a>
            <div class="dropdown-menu" aria-labelledby="navbarDropdown">
            <a class="dropdown-item" href="{% url 'uploadpdf' %}">अपलोड मिडिया फाईल</a>
            <div class="dropdown-divider"></div>
            <a class="dropdown-item" href="{% url 'uploadimage' %}">अपलोड फोटो</a>
            <div class="dropdown-divider"></div>
            <a class="dropdown-item" href="{% url 'undercons' %}">मीटिंग</a>
            </div>
        </li>
        
        <li class="nav-item">
            <a class="nav-link" href="{% url 'signup' %}">लॉग-इन</a>
        </li>
        
        </ul>
        <form class="form-inline my-2 my-lg-0">
        <input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search">
        <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
        </form>
    </div>
</nav>