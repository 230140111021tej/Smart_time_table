from ortools.sat.python import cp_model

def simple_schedule_demo():
    model = cp_model.CpModel()
    timeslots = range(2)
    rooms = range(2)
    classes = range(2)
    ts = {c: model.NewIntVar(0, 1, f"ts_{c}") for c in classes}
    rm = {c: model.NewIntVar(0, 1, f"rm_{c}") for c in classes}
    for i in classes:
        for j in classes:
            if i < j:
                b = model.NewBoolVar(f"diff_{i}_{j}")
                model.Add(ts[i] != ts[j]).OnlyEnforceIf(b)
                model.Add(rm[i] != rm[j]).OnlyEnforceIf(b.Not())
    solver = cp_model.CpSolver()
    status = solver.Solve(model)
    if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
        result = []
        for c in classes:
            result.append({"class_id": c, "timeslot": solver.Value(ts[c]), "room": solver.Value(rm[c])})
        return result
    else:
        return []
