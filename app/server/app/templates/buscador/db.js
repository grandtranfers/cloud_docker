/* XSearch version 5.2 - Database file */

/* configuration settings */

	searchname = 'index.html'
	
	usebannercode=true
	/*ButtonCode = "<img src='searchbutton.gif' border=0>" */
	ButtonCode = "<div class='btn'><i class='fa fa-search'></i></div>" 
	
	function templateBody() {
		document.write('<html><head><title>XSearch1'+version+'</title><'+
		'script language="Javascript">'+
		'</script'+'></head><body><table border="0px" width="80%" align="center"><tr><td><center><font face=Verdana size=12 color="blue"><b>Buscador </b><i>XSearch 5.2</i></font>  </center></td></tr> ');
	}

	function templateEnd() {
		document.write('</font></div></table></body></html>');
	}
	function bannerCode() {
	}	

/* end configuration settings */

/* database records */

add("<a href='https://developer.mozilla.org/es/docs/Web/HTML'  target='_ blank'>HTML: Lenguaje de etiquetas de hipertexto</a>","html css javascript","descripción visible en pantalla..descripción visible en pantalla.<br>..otrodescripción visible en pantalla.descripción visible en pantalla.")
add("<a href='http://www.defensor-alejo.com.ar/legis/nacion_doc/00340-cod-civil.zip 'target='_ blank' >Título con Hipervínculo</a>","javascript java desarrolo web","descripción para presentar..<br>..otro")
add("<a href='http://www.dynamic-core.net/jsvcl/vcl2/index.htm' target='_ blank'>Título con Hipervínculo</a>","En éste campo están permitidos todos los caracteres menos el enter","descripción visibe<br>poner un listado de nombres y de e-mail para las guías")

/* end database records */