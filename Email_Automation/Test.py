import extract_msg, glob, csv



def get_answer_from_next_line(file_in, text_in):
    temp = []
    for i, line in enumerate(file_in.splitlines()):
        if text_in in ('Will anyone else be living with you when you move?', 'Will anyone else live with you when you move?'):
            if text_in in line:
                temp.append(file_in.splitlines()[i+1])

                return temp
                #return temp
                #print(temp)
        elif text_in in 'Have you (main applicant) lived at another addresses over the past 3 years?':
            if text_in in line:
                temp.append(file_in.splitlines()[i + 1])
                if 'Yes' in file_in.splitlines()[i+1]:
                    for z in Info2:
                        temp.append(get_answer_from_line(file_in,z))
                else:
                    for l in range(5):
                        temp.append('')
                        return temp
                        #return temp
                        #print(temp)
        elif text_in in '4.  National Insurance number':
            if text_in in line:
                if '5.  Relationship to main applicant:' in file_in.splitlines()[i+1]:
                    temp.append('')
                    return temp
                else:
                    temp.append(file_in.splitlines()[i+1])
                    return temp
        elif text_in in line:
            temp.append(file_in.splitlines()[i+1])
            #print(temp)
            return temp






def get_answer_from_line(file_in, text_in):
    iterator = iter(file_in.splitlines())
    try:
        for line in iterator:
            temp = ''
            temp = next(x for x in iterator if text_in in x)
            temp = temp.split(': ')
            return temp[-1]
    except:
        return('NA')






if __name__ == '__main__':
    Information_Line = ['2.  Gender', '3.  Date of Birth', '4.  National Insurance number', '5.  Contact Email address',
    '6.  Contact Number', '7.  Are you pregnant/expecting a baby?',
    '8.  Please indicate which option most closely describes your ethnic origin',
    '9.  What is your preferred language?', 'What is your connection to Tameside?',
    'Do you have the Right to Rent?',
    'When did you move to this address?', 'Reason for housing need', 'Current property type',
    'Tenure at your current address', 'Please provide Landlord details:',
    'Number of bedrooms in the property',
    'How many of these bedrooms do you and your family have use of?',
    'Have you (main applicant) lived at another addresses over the past 3 years?', '10. Address'
    'Are you interested in Independent living & 55+ properties?',
    'Have you or anyone who will be living with you been evicted from a Jigsaw Homes, Council or Registered Provider tenancy within the last 3 years for any tenancy breaches?',
    'Do you or anyone who will be living with you have any unspent convictions or currently subject to any criminal investigations?',
    'Is anybody in the moving group in employment?', 'Is anybody in the moving group volunteering?',
    'Is anybody in the moving group in receipt of Carers Allowance for a person outside of your household?',
    'Is anybody in the moving group in receipt of Fostering Allowance?',
    'Is anybody in the moving group a serving or discharged member of The Armed Forces?',
    'Are you or anybody in the moving group related to a member of staff or board member for Jigsaw Homes?',
    'Will anyone else be living with you when you move?']
    # ,'Please use this space to add any further information you feel may assist your application:']
    Information = ['Prefix : ', 'First Name : ', 'Last Name : ']
    Info2 = ['Street Address : ', 'City : ', 'State : ', 'Zip : ', 'Country: ']
    People_After = ['Gender', 'Date of Birth', '4.  National Insurance number', 'Relationship to main applicant:',
    'Would you like this applicant to be a joint applicant with you?',
    'Does this person currently live at a different address from the main applicant?',
    'Is this person a British or Commonwealth Citizen with the right of abode in the UK',
    'Does this person have indefinite leave to remain in the UK?',
    'Does this person have indefinite leave to remain in the UK',
    'Will anyone else live with you when you move?']
    f = open('test.csv', 'w')
    writer = csv.writer(f)
    for msg in glob.glob('Emails\*.msg'):
        with extract_msg.openMsg(msg) as msg:
            body_text = msg.body
            count = []
            for y in Information:
                count.append(get_answer_from_line(body_text, y))
                body_text = body_text.replace(y, '', 1)
            for Current in Information_Line:
                if Current in 'When did you move to this address?':
                    for z in Info2:
                        count.append(get_answer_from_line(body_text, z))
                        body_text = body_text.replace(y, '', 1)
                count.append(get_answer_from_next_line(body_text, Current))
                body_text = body_text.replace(Current, '', 1)
                if Current in 'Will anyone else be living with you when you move?':
                    del count[-1]
                    for t in range(6):
                        if 'Yes (please complete the information required below)' or 'Yes (please complete the information required below)' or 'Yes ' in count[-1]:
                            for y in Information:
                                count.append((get_answer_from_line(body_text, y)))
                                body_text = body_text.replace(y, '', 1)
                            for z in People_After:
                                count.append(get_answer_from_next_line(body_text, z))
                                body_text = body_text.replace(z, '', 1)

            writer.writerow(count)
    f.close()