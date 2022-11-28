from operator import invert
from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.

def main_page(request):
	return redirect(room)

def room(request):
	error = ''

	if 'submitProd' in request.POST:
		form = RoomForm(request.POST)
		if form.is_valid():
			form.save()
		else:
			error = 'Form is not valid'

	if 'Edit' in request.POST:
		record_id = request.POST.get('Edit')
		return redirect(room_edit, id=record_id)

	if 'Delete' in request.POST:
		record_id = request.POST.get('Delete')
		record = Room.objects.get(id = record_id)
		record.delete()

	rooms = Room.objects.order_by('phone')
	form = RoomForm()
	context = {
		'form': form,
		'error': error
	}

	return render(request, 'main/Rooms.html', {'rooms': rooms, 'context': context})


def helthy(request):
	error = ''

	if 'submit' in request.POST:
		form = HealthyForm(request.POST)
		if form.is_valid():
			form.save()
		else:
			error = 'Form is not valid'

	helthies = Healthy.objects.order_by('medCard')
	form = HealthyForm()
	context = {
		'form': form,
		'error': error
	}

	return render(request, 'main/Healthy.html', {'helthies': helthies, 'context': context})


def move(request):
	error = ''

	if 'submit' in request.POST:
		form = MoveForm(request.POST)
		if form.is_valid():
			form.save()
		else:
			error = 'Form is not valid'

	if 'Delete' in request.POST:
		record_id = request.POST.get('Delete')
		record = Move.objects.get(id = record_id)
		record.delete()

	moves = Move.objects.order_by('room')
	form = MoveForm()
	context = {
		'form': form,
		'error': error
	}

	return render(request, 'main/Moves.html', {'moves': moves, 'context': context})

def room_edit(request, id):
	error = ''
	record = Room.objects.get(id = id)

	if 'submitEdit' in request.POST:
		form = RoomForm(request.POST)

		if form.is_valid():
			if form.data['phone']:
				record.phone = form.data['phone']

			record.save()

			return redirect(room)
		else:
			error = 'Form is not valid'

	form = RoomForm()
	context = {
		'form': form,
		'error': error
	}

	return render(request, 'main/RoomsEdit.html', {'record': record, 'context': context})


def medCard(request):
	error = ''

	if 'submit' in request.POST:
		form = MedCardForm(request.POST)
		if form.is_valid():
			form.save()
		else:
			error = 'Form is not valid'

	if 'Edit' in request.POST:
		record_id = request.POST.get('Edit')
		return redirect(medCard_edit, id = record_id)

	if 'Delete' in request.POST:
		record_id = request.POST.get('Delete')
		record = MedCard.objects.get(id = record_id)
		record.delete()

	med_cards = MedCard.objects.order_by('name')

	form = MedCardForm()
	context = {
		'form': form,
		'error': error
	}

	return render(request, 'main/MedCard.html', {'med_cards': med_cards, 'context': context})


def medCard_edit(request, id):
	error = ''
	record = MedCard.objects.get(id = id)

	if 'submitEdit' in request.POST:
		form = MedCardForm(request.POST)
		if form.is_valid():
			if form.data['name']:
				record.name = form.data['name']
			if form.data['diagnos']:
				record.diagnos = form.data['diagnos']
			if form.data['cause']:
				record.cause = form.data['cause']
			if form.data['other']:
				record.other = form.data['other']
			if form.data['gender']:
				record.gender = form.data['gender']
			if form.data['age']:
				record.age = form.data['age']
			if form.data['date']:
				record.date = form.data['date']

			record.save()

			return redirect(medCard)
		else:
			error = 'Form is not valid'

	form = MedCardForm()
	context = {
		'form': form,
		'error': error
	}

	return render(request, 'main/MedCardEdit.html', {'record': record, 'context': context})

def medCardOfDate(request):
	error = ''
	records = []

	if 'search' in request.POST:
		form = MedCardOfDataForm(request.POST)
		if form.is_valid():
			date = form.data['date']
			date = date.split('/')
			for i in range(3):
				date[i] = int(date[i])
			date = datetime(date[2], date[1], date[0]).date()
			for m in MedCard.objects.raw("""
				SELECT * FROM `main_medcard` WHERE `main_medcard`.`date`<=%s
			""", [date]):
				dates = Healthy.objects.filter(medCard=m.id).order_by('date')
				if (dates and dates[0].date > date) or not dates:
					m.room = getRoom(m)
					records.append(m)
		else:
			error = 'Form is not valid'

	form = MedCardOfDataForm()
	context = {
		'form': form,
		'error': error
	}
	return render(request, 'main/MedCardOfData.html', {'records': records, 'context': context})

def medCardOfAge(request):
	error = ''
	records = []

	if 'search' in request.POST:
		form = MedCardOfAgeForm(request.POST)
		if form.is_valid():
			age = form.data['age']
			for m in MedCard.objects.raw("""
				SELECT * FROM `main_medcard` WHERE `main_medcard`.`age`>%s
			""", [age]):
				if not Healthy.objects.filter(medCard=m):
					records.append(m)
		else:
			error = 'Form is not valid'

	form = MedCardOfAgeForm()
	context = {
		'form': form,
		'error': error
	}
	return render(request, 'main/MedCardOfAge.html', {'records': records, 'context': context})

def roomOfMedCard(request):
	error = ''
	rooms = []

	if 'search' in request.POST:
		form = RoomOfMedCardForm(request.POST)
		if form.is_valid():
			name = MedCard.objects.filter(name=form.data['name'])
			for m in name:
				room = getRoom(m)
				rooms.append(room)
		else:
			error = 'Form is not valid'

	form = RoomOfMedCardForm()
	context = {
		'form': form,
		'error': error
	}
	return render(request, 'main/RoomOfMedCard.html', {'rooms': rooms, 'context': context})

def getRoom(medCard):
	if not Healthy.objects.filter(medCard=medCard):
		room = Move.objects.filter(medCard=medCard).order_by('date')
		if room:
			room = room[len(room)-1].room
			return room