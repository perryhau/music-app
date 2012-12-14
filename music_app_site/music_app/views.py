from django.http import HttpResponse
from django.shortcuts import render_to_response
from django import forms
from django.shortcuts import render
from django.http import HttpResponseRedirect
from music21 import *


#forms 

class MusicSearchForm(forms.Form):
	time_signature_choices = (('', ''), ('1', '3/4'),('2', '4/4'),('3', '6/8'))
	min_tempo_choices = (('', ''), ('2', '40'),('3', '50'),('4', '60'),
		('5', '70'),('6', '80'),('7', '90'),('8', '100'),
		('9', '120'),('10', '130'),('11', '140'),('12', '150'),
		('13', '160'),('14', '170'),('15', '180'))
	max_tempo_choices = (('', ''), ('2', '40'),('3', '50'),('4', '60'),
		('5', '70'),('6', '80'),('7', '90'),('8', '100'),
		('9', '120'),('10', '130'),('11', '140'),('12', '150'),
		('13', '160'),('14', '170'),('15', '180'))
	pre_progression_choices = (('', ''), ('1', 'II'), ('2', 'V'),('3', 'I'), 
		('4', 'IV'),('5', 'VII'), ('6', 'III'),('7', 'VI'))
	progression_choices = (('', ''), ('1', 'II'), ('2', 'V'),('3', 'I'), 
		('4', 'IV'),('5', 'VII'), ('6', 'III'),('7', 'VI'))
	post_progression_choices = (('', ''), ('1', 'II'), ('2', 'V'),('3', 'I'), 
		('4', 'IV'),('5', 'VII'), ('6', 'III'),('7', 'VI'))
	pre_root_choices = (('', ''), ('1', 'C'), ('2', 'C#/Db'), ('3', 'D'), 
		('4', 'D#/Eb'), ('5', 'E'), ('6', 'F'), ('7', 'F#/Gb'), ('8', 'G'), ('9', 'G#/Ab')
		, ('10', 'A'), ('11', 'A#/Bb'), ('12', 'B'))
	root_choices = (('', ''), ('1', 'C'), ('2', 'C#'), ('3', 'D'), 
		('4', 'D#'), ('5', 'E'), ('6', 'F'), ('7', 'F#'), ('8', 'G'), ('9', 'G#')
		, ('10', 'A'), ('11', 'A#'), ('12', 'B'))
	post_root_choices = (('', ''), ('1', 'C'), ('2', 'C#'), ('3', 'D'), 
		('4', 'D#'), ('5', 'E'), ('6', 'F'), ('7', 'F#'), ('8', 'G'), ('9', 'G#')
		, ('10', 'A'), ('11', 'A#'), ('12', 'B'))

	time_signature = forms.ChoiceField(time_signature_choices, required=False)
	min_tempo = forms.ChoiceField(min_tempo_choices, required=False)
	max_tempo = forms.ChoiceField(max_tempo_choices, required=False)
	progression = forms.ChoiceField(progression_choices, required=False)
	pre_progression = forms.ChoiceField(pre_progression_choices, required=False)
	post_progression = forms.ChoiceField(post_progression_choices, required=False)
	root = forms.ChoiceField(root_choices, required=False)
	pre_root = forms.ChoiceField(pre_root_choices, required=False)
	post_root = forms.ChoiceField(post_root_choices, required=False)
	


#views



def index(request):
	stuff = 'stuff views.py'
	return render_to_response('index.html', {'contact_list':stuff})

def counterpoint(request):
	return render_to_response('counterpoint.html')
	
def improvisation(request):
	'''ADD IN: song choice, narrow down to beat andn note '''
	if request.method == 'POST':
		form = MusicSearchForm(request.POST)
		if form.is_valid():
			time_signature = form.cleaned_data['time_signature']
			min_tempo = form.cleaned_data['min_tempo']
			max_tempo = form.cleaned_data['max_tempo']
			pre_progression = form.cleaned_data['pre_progression']
			progression = form.cleaned_data['progression']
			post_progression = form.cleaned_data['post_progression']
			pre_root = form.cleaned_data['pre_root']
			root = form.cleaned_data['root']
			post_root = form.cleaned_data['post_root']
			print 'Time signature: ', time_signature
			print 'Min Tempo: ', min_tempo
			print 'Max Tempo', max_tempo
			print 'Pre Progression: ', pre_progression
			print 'Progression: ', progression
			print 'Post Progression: ', post_progression
			print 'Pre root: ', pre_root
			print 'Root: ', root
			print 'Post Root: ', post_root

			return HttpResponseRedirect('/music_app/improvisation')
	else:
		form = MusicSearchForm()

	return render(request, 'improvisation.html', {'form':form,})

def orchestration(request):
	return render_to_response('orchestration.html')

def documentation(request):
	return render_to_response('documentation.html')