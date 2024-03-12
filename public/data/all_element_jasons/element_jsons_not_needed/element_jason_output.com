gfx re no output
gfx re el output

gfx edit scene
gfx cre win
gfx mod win 1 set pert

#@posterior_elements_list = (249..252); #NB - initially used this line for testing

#@posterior_elements_list = (249..252,256,261..265,269..272,321..324,369..372,377..378,383..384,391..398,408..413,424..429,440..445,456..461,472..477,488..493,504..509,520..525,536..541)
#push @posterior_elements_list, 553..556,574..579,590..595,604..607,611,614..615,618..619,622..623,626..627,630..631,635,638..639,643,647,651,655,659,662..663,666..667,670..674,680..681;
#push @posterior_elements_list, 688..693,700..704,707..709,715..717,724..726,732..733,737,739..740,748,751..752,755..756,759..760,763,767..768,771..772,775..776,779..780,783,787..788,791,795;
#push @posterior_elements_list, 799,803..804,810,813..818,825..830,837..842,851..854,860..862,868..870,875..877,884..885;
@anterior_elements_list = (258..260,273..275,317..320,365..368,373..376,379..382,387..390,399..406,415..422,431..438,447..454,463..470,479..486,495..502,511..518,527..534,543..550,559..573)
	push @anterior_elements_list, 580..589,596..603,608..610,612..613,616..617,621,624..625,628..629,633,636..637,640..641,645,648..649,652..653,656..657,660..661,664..665,668..669,675..678;
	push @anterior_elements_list, 682..686,694..698,705..706,711..714,719..722,727..730,736,743..746,749..750,753..754,757..758,761..762,765..766,769,773,777..778,781..782,785,789,793;
	push @anterior_elements_list, 797..798,801..802,806..809,811..812,820..824,832..836,844..847,855..858,863..866,871..874,879..881;

gfx create egroup current_element;
gfx modify g_element current_element surfaces select_on material red selected_material default_selected render_shaded;

for $i(@anterior_elements_list){
	gfx select element $i;
	gfx modify egroup current_element add $i;
	gfx export threejs file_prefix $i data_export_colour;
	gfx unselect element $i;		
	gfx modify egroup current_element rem $i;
}
