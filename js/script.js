document.getElementById("header-placeholder").innerHTML = 
`<div id="name_logo" class="row">
	<div class="col m2 hide-on-small-only"> 
		<div class="right">
			<img class="responsive-img" src="images/CEG_logo.png" width="100" height="100" alt="CEG logo">
		</div>
	</div>
	<div class="col s12 m8">
		<div class="center-align">
			<h4>Department of Electronics and Communication</h4>
			<h6><a href="https://www.annauniv.edu/" target="_blank">Anna university</a></h6>
		</div>
	</div>
	<div class="col m2 l2 hide-on-small-only"></div>
</div>
<div class="divider"></div>
<div class="row">
	<div id="nav_bar">
	<nav class="z-depth-0">
		<div class="nav-wrapper">
			<a class="brand-logo left" href="/" class="left"><i class="material-icons">home</i></a>
			<a href="#" data-activates="mobile-demo" class="button-collapse right"><i class="material-icons">menu</i></a>
			<ul id="nav-mobile" class="right hide-on-med-and-down">
				<li><a class="dropdown-button" data-constrainwidth="false" data-hover="true" data-beloworigin="true" data-activates="acad" href="#!">ACADEMICS<i class="material-icons right">arrow_drop_down</i></a></li>
				<li><a class="dropdown-button" data-constrainwidth="false" data-hover="true" data-beloworigin="true" data-activates="people" href="#!">PEOPLE<i class="material-icons right">arrow_drop_down</i></a></li>
				<li><a href="/infra">INFRASTRUCTURE</a></li>
				<li><a class="dropdown-button" data-constrainwidth="false" data-hover="true" data-beloworigin="true" data-activates="acti" href="#!">ACTIVITIES<i class="material-icons right">arrow_drop_down</i></a></li>
				<li><a href="/research">RESEARCH</a></li>
				<li><a href="/ecea">ECEA</a></li>
				<li><a href="/placements">PLACEMENTS</a></li>
				<li><a href="/contact">CONTACT US</a></li>
				<li><a href="/forum">FORUM</a></li>
			</ul>
			<ul class="side-nav" id="mobile-demo">
				<ul class="collapsible">
					<li><a class="collapsible-header" href="#!">ACADEMICS<i class="material-icons right">arrow_drop_down</i></a>
			            <div class="collapsible-body">
           					<ul>
								<li><a href="/ug">UG Programs</a></li>
								<li><a href="/pg">PG Programs</a></li>
								<li><a href="/part">Part-time</a></li>
           					</ul>
           				</div>
					</li>
				</ul>
				<ul class="collapsible">
					<li><a class="collapsible-header" href="#!">PEOPLE<i class="material-icons right">arrow_drop_down</i></a>
			            <div class="collapsible-body">
           					<ul>
								<li><a href="/staff">Teaching Staff</a></li>
								<li><a href="/nstaff">Non-Teaching Staff</a></li>
								<li><a href="/students">Students</a></li>
           					</ul>
           				</div>
					</li>
				</ul>							
				<li><a href="/infra">INFRASTRUCTURE</a></li>
				<ul class="collapsible">
					<li><a class="collapsible-header" href="#!">ACTIVITIES<i class="material-icons right">arrow_drop_down</i></a>
			            <div class="collapsible-body">
           					<ul>
	 							<li><a href="/workshop">Workshops</a></li>
	 							<li><a href="/fv">Foriegn visits</a></li>
       						</ul>
       					</div>
					</li>
				</ul>
				<li><a href="/research">RESEARCH</a></li>														
				<li><a href="/ecea">ECEA</a></li>
				<li><a href="/placements">PLACEMENTS</a></li>
				<li><a href="/contact">CONTACT US</a></li>
				<li><a href="/forum">FORUM</a></li>
			</ul>
			<ul id="acad" class="dropdown-content">
				<li><a href="/ug">UG Programs</a></li>
				<li><a href="/pg">PG Programs</a></li>
				<li><a href="/part">Part-time</a></li>
			</ul>
			<ul id="people" class="dropdown-content">
				<li><a href="/staff">Teaching Staff</a></li>
				<li><a href="/nstaff">Non-Teaching Staff</a></li>
				<li><a href="/students">Students</a></li>
			</ul>
			<ul id="acti" class="dropdown-content">
				<li><a href="/workshop">Workshops</a></li>
				<li><a href="/fv">Foriegn visits</a></li>
			</ul>
		</div>
	</nav>
	</div>
	<div id="gap" style="display:none; height:64px; width:100%">
	</div>
</div>
<br>`;

$(document).ready(function() {
  var result = $("#name_logo").height();
  $(window).scroll(function () {
      //if you hard code, then use console
      //.log to determine when you want the 
      //nav bar to stick.  
      console.log($(window).scrollTop())
    if ($(window).scrollTop() > result) {
      $('#nav_bar').addClass('navbar-fixed-top');
      $('#gap').css("display","block")
    }
    if ($(window).scrollTop() < (result + 1)) {
      $('#nav_bar').removeClass('navbar-fixed-top');
      $('#gap').css("display","none")
    }
  });
});