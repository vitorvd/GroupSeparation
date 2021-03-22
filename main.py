from group import Group
import csv


def generate_groups():
    groups = [Group(1)]
    group_ref = groups[0]

    with open('cadastros.csv', newline='', encoding='utf-8') as file:
        csv_reader = csv.reader(file, delimiter=',')

        csv_reader.__next__()  # pular a primeira linha, tendo em vista que são os nomes das colunas

        for row in csv_reader:
            added = group_ref.addParticipant(row[1], row[5], row[6])
            if not added:
                while not added:
                    groups.append(Group(len(groups) + 1))
                    group_ref = groups[len(groups) - 1]
                    added = group_ref.addParticipant(row[1], row[5], row[6])

    def generate_csv():
        nonlocal groups

        with open('grupos.csv', 'w', newline='', encoding='utf-8') as file:

            writer = csv.writer(file, delimiter=',')

            for group in groups:
                writer.writerow(["Grupo", "Nome", "Contato","Experiência"])
                for participant in group.participants:
                    writer.writerow([group.tag, participant.name, participant.contact.strip(), participant.experience])

    return generate_csv()


generate_groups()
