from django.shortcuts import render, redirect
from .forms import Calculator


def calculator(request):
    form = Calculator()

    if request.method == "POST":
        form = Calculator(request.POST)

        if form.is_valid():
            a = form.cleaned_data["first_number"]
            b = form.cleaned_data["second_number"]
            operation = form.cleaned_data["chose_function"]

            if operation == "add":
                result = a + b
            elif operation == "subtract":
                result = a - b
            elif operation == "multiply":
                result = a * b
            elif operation == "divide":
                if b == 0:
                    form.add_error("second_number", "На ноль делить нельзя.")
                    result = None
                else:
                    result = a / b
            else:
                result = None

            if result is not None:
                request.session["calculator_result"] = {
                    "first_number": a,
                    "second_number": b,
                    "operation": operation,
                    "result": result,
                }
                return redirect("calculator_result")

    return render(request, "calculator.html", {"form": form})


def calculator_result(request):
    data = request.session.get("calculator_result")

    if not data:
        return redirect("calculator")

    return render(request, "calculator_result.html", {"data": data})