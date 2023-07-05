import extract_msg, glob, csv



def get_answer_from_next_line(file_in, text_in):
    temp = []
    for i, line in enumerate(file_in.splitlines()):
        if text_in in ('Will anyone else be living with you when you move?', 'Will anyone else live with you when you move?'):
            if text_in in line and (file_in.splitlines()[i+1] == 'Yes'):
                #print(file_in.splitlines()[i+1])
                temp.append(file_in.splitlines()[i+1])
                print(temp)

        elif text_in in 'Have you (main applicant) lived at another addresses over the past 3 years?':
            if text_in in line:
                #print(file_in.splitlines()[i + 1])
                temp.append(file_in.splitlines()[i + 2])
                print(temp)
                for z in Info2:
                    #print('hello')
                    #print(get_answer_from_line(body_text, z))
                    temp.append(get_answer_from_line(body_text,z))
                    print(temp)
                    #body_text = body_text.replace(z, '', 1)

        elif text_in in line:
            if str((file_in.splitlines()[i+1])) not in ('5.  Relationship to main applicant:', '7.  Number of bedrooms in the property', '9.  ?'):
                #print(file_in.splitlines()[i + 1])
                temp.append(file_in.splitlines()[i + 1])
                print(temp)
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
        return('N/A')






if __name__ == '__main__':
    #with open('test.csv', 'w', encoding='UTF8') as f:
        #writer = csv.writer(f)
        #writer.writerow()
    for msg in glob.glob('*.msg'):
        with extract_msg.openMsg(msg) as msg:
            body_text = msg.body
            Msg_list = []
            Test_List = []
            count = 0
            Information_Line = ['2.  Gender', '3.  Date of Birth', '4.  National Insurance number', '5.  Contact Email address',
            '6.  Contact Number', '7.  Are you pregnant/expecting a baby?', '8.  Please indicate which option most closely describes your ethnic origin',
            '9.  What is your preferred language?', 'What is your connection to Tameside?', 'Do you have the Right to Rent?',
            'When did you move to this address?', 'Reason for housing need', 'Current property type',
            'Tenure at your current address', 'Please provide Landlord details:', 'Number of bedrooms in the property',
            'How many of these bedrooms do you and your family have use of?', 'Have you (main applicant) lived at another addresses over the past 3 years?', '10. Address'
            'Are you interested in Independent living & 55+ properties?', 'Have you or anyone who will be living with you been evicted from a Jigsaw Homes, Council or Registered Provider tenancy within the last 3 years for any tenancy breaches?',
            'Do you or anyone who will be living with you have any unspent convictions or currently subject to any criminal investigations?',
            'Is anybody in the moving group in employment?', 'Is anybody in the moving group volunteering?', 'Is anybody in the moving group in receipt of Carers Allowance for a person outside of your household?',
            'Is anybody in the moving group in receipt of Fostering Allowance?', 'Is anybody in the moving group a serving or discharged member of The Armed Forces?',
            'Are you or anybody in the moving group related to a member of staff or board member for Jigsaw Homes?', 'Will anyone else be living with you when you move?']
            #,'Please use this space to add any further information you feel may assist your application:']
            Information = ['Prefix : ', 'First Name : ', 'Last Name : ']
            Info2 = ['Street Address : ', 'City : ', 'State : ', 'Zip : ', 'Country: ']
            PersonList = ['Person Two', 'Person Three', 'Person Four', 'Person Five', 'Person Six']
            People_After = ['Gender', 'Date of Birth', '4.  National Insurance number', 'Relationship to main applicant:', 'Would you like this applicant to be a joint applicant with you?',
            'Does this person currently live at a different address from the main applicant?','Is this person a British or Commonwealth Citizen with the right of abode in the UK',
            'Does this person have indefinite leave to remain in the UK?','Does this person have indefinite leave to remain in the UK','Will anyone else live with you when you move?']
            iterator2 = iter(PersonList)
            Test_List.clear()
            for y in Information:
                Msg_list.append((get_answer_from_line(body_text, y)))
                body_text = body_text.replace(y, '', 1)
            #print(' '.join(Msg_list))
            Msg_list.clear()

            for z in Info2:
                Test_List = get_answer_from_line(body_text, z)
                body_text = body_text.replace(z, '', 1)
                #print(Test_List)
            for Current in Information_Line:
                Test_List = get_answer_from_line(body_text, Current)
                #print(Test_List)
                body_text = body_text.replace(Current, '', 1)

            print(next(iterator2))
            for count in range(0, 6):
                for person in PersonList:
                    try:
                        for y in Information:
                            Msg_list.append((get_answer_from_line(body_text, y)))
                            body_text = body_text.replace(y, '', 1)
                        #print(' '.join(Msg_list))
                        Msg_list.clear()

                        for Current in People_After:
                            Test_List = get_answer_from_line(body_text, z)
                            #print(Test_List)
                            body_text = body_text.replace(Current, '', 1)
                        if person in body_text:
                            print(next(iterator2))
                    except:
                        body_text = body_text