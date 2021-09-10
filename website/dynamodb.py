import boto3
from boto3.dynamodb.conditions import Key

session = boto3.Session(
    aws_access_key_id = "YOUR_AWS_ACCESS_KEY_ID",
    aws_secret_access_key = "YOUR_AWS_SECRET_ACCESS_KEY"
)

dynamodb = session.resource('dynamodb', region_name="us-east-2")
table = dynamodb.Table('MyAttorneyArticles')

def put_data(data):
    table.put_item(Item=data)

def get_data(articleNumber):
    response = table.query(
        KeyConditionExpression=Key('articleNumber').eq(articleNumber)
    )
    if(len(response["Items"]) != 0):
        return response['Items'][0]["description"]
    return ""


if __name__ == '__main__':
    descrip = [
        """<b>Name and territory of the Union.</b>
<br>(1) India, that is Bharat, shall be a Union of States.
<br>(2) The States and the territories thereof shall be as specified in the First Schedule.]
<br>(3) The territory of India shall comprise—
<br>(a) the territories of the States;
<br>(b) the Union territories specified in the First Schedule; and
<br>(c) such other territories as may be acquired.""",

    """<b>Admission or establishment of new States</b> Parliament may by law admit into the Union, or
establish, new States on such terms and conditions as it thinks fit. """,

    """ <b>Formation of new States and alteration of areas, boundaries or names of existing States.</b>—
<br>Parliament may by law—
<br>(a) form a new State by separation of territory from any State or by uniting two or more States or
<br>parts of States or by uniting any territory to a part of any State;
<br>(b) increase the area of any State;
<br>(c) diminish the area of any State;
<br>(d) alter the boundaries of any State;
<br>(e) alter the name of any State:
<br>Provided that no Bill for the purpose shall be introduced in either House of Parliament except on the
recommendation of the President and unless, where the proposal contained in the Bill affects the area,
boundaries or name of any of the States
, the Bill has been referred by the President to the Legislature of that
State for expressing its views thereon within such period as may be specified in the reference or within such
<br>further period as the President may allow and the period so specified or allowed has expired.""",

    """
<b>Laws made under articles 2 and 3 to provide for the amendment of the First and the Fourth
Schedules and supplemental, incidental and consequential matters.</b>—
<br>(1) Any law referred to in article 2 or article 3 shall contain such provisions for the amendment of the First Schedule and the Fourth Schedule
as may be necessary to give effect to the provisions of the law and may also contain such supplemental,
incidental and consequential provisions (including provisions as to representation in Parliament and in the
Legislature or Legislatures of the State or States affected by such law) as Parliament may deem necessary.
<br>(2) No such law as aforesaid shall be deemed to be an amendment of this Constitution for the purposes
of article 368.
    """,


    """
<b>Citizenship at the commencement of the Constitution</b>.—At the commencement of this
Constitution, every person who has his domicile in the territory of India and—
<br>(a) who was born in the territory of India; or
<br>(b) either of whose parents was born in the territory of India; or
<br>(c) who has been ordinarily resident in the territory of India for not less than five years immediately
preceding such commencement,
shall be a citizen of India.
    """,

    """
<b>Rights of citizenship of certain persons who have migrated to India from Pakistan.</b>-
Notwithstanding anything in article 5, a person who has migrated to the territory of India from the territory
now included in Pakistan shall be deemed to be a citizen of India at the commencement of this Constitution
if—
<br>(a) he or either of his parents or any of his grand-parents was born in India as defined in the
Government of India Act, 1935 (as originally enacted); and
<br>(b) (i) in the case where such person has so migrated before the nineteenth day of July, 1948, he has
been ordinarily resident in the territory of India since the date of his migration, or
<br>(ii) in the case where such person has so migrated on or after the nineteenth day of July, 1948, he has
been registered as a citizen of India by an officer appointed in that behalf by the Government of the
Dominion of India on an application made by him therefor to such officer before the commencement of
this Constitution in the form and manner prescribed by that Government:
<br>Provided that no person shall be so registered unless he has been resident in the territory of India for
at least six months immediately preceding the date of his application
    """,
    """
<b>Rights of citizenship of certain migrants to Pakistan.</b>—Notwithstanding anything in articles 5 and
6, a person who has after the first day of March, 1947, migrated from the territory of India to the territory
now included in Pakistan shall not be deemed to be a citizen of India:
<br>(a)Provided that nothing in this article shall apply to a person who, after having so migrated to the territory
now included in Pakistan, has returned to the territory of India under a permit for resettlement or permanent
return issued by or under the authority of any law and every such person shall for the purposes of clause 
<br>(b) of article 6 be deemed to have migrated to the territory of India after the nineteenth day of July, 1948.

    """,

    """
    <b>Rights of citizenship of certain persons of Indian origin residing outside India.</b>—Notwithstanding
anything in article 5, any person who or either of whose parents or any of whose grand-parents was born in
India as defined in the Government of India Act, 1935 (as originally enacted), and who is ordinarily residing
in any country outside India as so defined shall be deemed to be a citizen of India if he has been registered as
a citizen of India by the diplomatic or consular representative of India in the country where he is for the time
being residing on an application made by him therefor to such diplomatic or consular representative, whether
before or after the commencement of this Constitution, in the form and manner prescribed by the
Government of the Dominion of India or the Government of India
    """,
    """
    <b>Persons voluntarily acquiring citizenship of a foreign State not to be citizens.</b>— No person shall
be a citizen of India by virtue of article 5, or be deemed to be a citizen of India by virtue of article 6 or article
8, if he has voluntarily acquired the citizenship of any foreign State.
    """,
    """
    <b>Continuance of the rights of citizenship.</b>—Every person who is or is deemed to be a citizen of
India under any of the foregoing provisions of this Part shall, subject to the provisions of any law that may
be made by Parliament, continue to be such citizen
    """,
    """
    <b>Parliament to regulate the right of citizenship by law.</b>—Nothing in the foregoing provisions of
this Part shall derogate from the power of Parliament to make any provision with respect to the acquisition
and termination of citizenship and all other matters relating to citizenship.
    """,
    """ <b>  Definition.</b>—In this Part, unless the context otherwise requires, ―the State‖ includes the Government
and Parliament of India and the Government and the Legislature of each of the States and all local or other
authorities within the territory of India or under the control of the Government of India""",
    """ <b> . Laws inconsistent with or in derogation of the fundamental rights.—</b>
<br>(1)All laws in force in the
territory of India immediately before the commencement of this Constitution, in so far as they are
inconsistent with the provisions of this Part, shall, to the extent of such inconsistency, be void.
<br>(2) The State shall not make any law which takes away or abridges the rights conferred by this Part and
any law made in contravention of this clause shall, to the extent of the contravention, be void.
<br>(3) In this article, unless the context otherwise requires,—
<br>(a) ―law‖ includes any Ordinance, order, bye-law, rule, regulation, notification, custom or usage
having in the territory of India the force of law;
<br>(b) ―laws in force‖ includes laws passed or made by a Legislature or other competent authority in the
territory of India before the commencement of this Constitution and not previously repealed,
notwithstanding that any such law or any part thereof may not be then in operation either at all or in
particular areas.
<br>[(4) Nothing in this article shall apply to any amendment of this Constitution made under article 368.]""",
    """ <b> Equality before law.—</b>The State shall not deny to any person equality before the law or the equal
protection of the laws within the territory of India.""",
""" <b> . Prohibition of discrimination on grounds of religion, race, caste, sex or place of birth</b>
<br>(1)The
State shall not discriminate against any citizen on grounds only of religion, race, caste, sex, place of birth or
any of them.
<br>(2) No citizen shall, on grounds only of religion, race, caste, sex, place of birth or any of them, be
subject to any disability, liability, restriction or condition with regard to—
<br>(a) access to shops, public restaurants, hotels and places of public entertainment; or
<br>(b) the use of wells, tanks, bathing ghats, roads and places of public resort maintained wholly or
partly out of State funds or dedicated to the use of the general public.
<br>(3) Nothing in this article shall prevent the State from making any special provision for women and
children.
<br>[(4) Nothing in this article or in clause (2) of article 29 shall prevent the State from making any special
provision for the advancement of any socially and educationally backward classes of citizens or for the
Scheduled Castes and the Scheduled Tribes.]

<br>[(5) Nothing in this article or in sub-clause (g) of clause (1) of article 19 shall prevent the State from
making any special provision, by law, for the advancement of any socially and educationally backward
classes of citizens or for the Scheduled Castes or the Scheduled Tribes in so far as such special provisions
relate to their admission to educational institutions including private educational institutions, whether aided
or unaided by the State, other than the minority educational institutions referred to in clause (1) of article
30.]

<br>[(6) Nothing in this article or sub-clause (g) of clause (1) of article 19 or clause (2) of article 29 shall
prevent the State from making,—
<br>(a) any special provision for the advancement of any economically weaker sections of citizens other than
the classes mentioned in clauses (4) and (5); and
<br>(b) any special provision for the advancement of any economically weaker sections of citizens other than
the classes mentioned in clauses (4) and (5) in so far as such special provisions relate to their admission to
educational institutions including private educational institutions, whether aided or unaided by the State,
other than the minority educational institutions referred to in clause (1) of article 30, which in the case of
reservation would be in addition to the existing reservations and subject to a maximum of ten per cent. of the
total seats in each category.
<br>Explanation.—For the purposes of this article and article 16, "economically weaker sections" shall be
such as may be notified by the State from time to time on the basis of family income and other indicators of
economic disadvantage.]""",

""" <b> Equality of opportunity in matters of public employment.— </b><br>(1) There shall be equality of
opportunity for all citizens in matters relating to employment or appointment to any office under the State.
<br>(2) No citizen shall, on grounds only of religion, race, caste, sex, descent, place of birth, residence or any of
them, be ineligible for, or discriminated against in respect of, any employment or office under the State.
<br>(3) Nothing in this article shall prevent Parliament from making any law prescribing, in regard to a class
or classes of employment or appointment to an office 3
[under the Government of, or any local or other
authority within, a State or Union territory, any requirement as to residence within that State or Union
territory] prior to such employment or appointment.
<br>(4) Nothing in this article shall prevent the State from making any provision for the reservation of
appointments or posts in favour of any backward class of citizens which, in the opinion of the State, is not
adequately represented in the services under the State.
<br>[(4A) Nothing in this article shall prevent the State from making any provision for reservation 5
[in
matters of promotion, with consequential seniority, to any class] or classes of posts in the services under the
State in favour of the Scheduled Castes and the Scheduled Tribes which, in the opinion of the State, are not
adequately represented in the services under the State.]
<br>
[(4B) Nothing in this article shall prevent the State from considering any unfilled vacancies of a year
which are reserved for being filled up in that year in accordance with any provision for reservation made
under clause (4) or clause (4A) as a separate class of vacancies to be filled up in any succeeding year or years
and such class of vacancies shall not be considered together with the vacancies of the year in which they are
being filled up for determining the ceiling of fifty per cent. reservation on total number of vacancies of that
year.]
<br>(5) Nothing in this article shall affect the operation of any law which provides that the incumbent of an office in connection with the affairs of any religious or denominational institution or any member of the
governing body thereof shall be a person professing a particular religion or belonging to a particular
denomination.
<br>[(6) Nothing in this article shall prevent the State from making any provision for the reservation of
appointments or posts in favour of any economically weaker sections of citizens other than the classes
mentioned in clause (4), in addition to the existing reservation and subject to a maximum of ten per cent. of
the posts in each category.]
 """,
""" <b> Abolition of Untouchability.</b>―Untouchability‖ is abolished and its practice in any form is
forbidden. The enforcement of any disability arising out of ―Untouchability‖ shall be an offence punishable
in accordance with law.""",
""" <b> Abolition of titles. </b><br>(1) No title, not being a military or academic distinction, shall be conferred by
the State.
<br>(2) No citizen of India shall accept any title from any foreign State.
<br>(3) No person who is not a citizen of India shall, while he holds any office of profit or trust under the
State, accept without the consent of the President any title from any foreign State.
<br>(4) No person holding any office of profit or trust under the State shall, without the consent of the
President, accept any present, emolument, or office of any kind from or under any foreign State""",
""" <b>Protection of certain rights regarding freedom of speech, </b><br>(1) All citizens shall have the
right—
<br>(a) to freedom of speech and expression;
<br>(b) to assemble peaceably and without arms;
<br>(c) to form associations or unions 2
[or co-operative societies];
<br>(d) to move freely throughout the territory of India;
<br>(e) to reside and settle in any part of the territory of India; 3
[and]
<br>(g) to practise any profession, or to carry on any occupation, trade or business.
<br>[(2) Nothing in sub-clause (a) of clause (1) shall affect the operation of any existing law, or prevent the
State from making any law, in so far as such law imposes reasonable restrictions on the exercise of the right
conferred by the said sub-clause in the interests of 6
[the sovereignty and integrity of India,] the security of
the State, friendly relations with foreign States, public order, decency or morality, or in relation to contempt
of court, defamation or incitement to an offence.]
<br>(3) Nothing in sub-clause (b) of the said clause shall affect the operation of any existing law in so far as
it imposes, or prevent the State from making any law imposing, in the interests of 6
[the sovereignty and
integrity of India or] public order, reasonable restrictions on the exercise of the right conferred by the said
sub-clause.<br>(4) Nothing in sub-clause (c) of the said clause shall affect the operation of any existing law in so far as
it imposes, or prevent the State from making any law imposing, in the interests of the sovereignty and
integrity of India or public order or morality, reasonable restrictions on the exercise of the right conferred by
the said sub-clause.
<br>(5) Nothing in 1
[sub-clauses (d) and (e)] of the said clause shall affect the operation of any existing law
in so far as it imposes, or prevent the State from making any law imposing, reasonable restrictions on the
exercise of any of the rights conferred by the said sub-clauses either in the interests of the general public or
for the protection of the interests of any Scheduled Tribe.
<br>(6) Nothing in sub-clause (g) of the said clause shall affect the operation of any existing law in so far as
it imposes, or prevent the State from making any law imposing, in the interests of the general public,
reasonable restrictions on the exercise of the right conferred by the said sub-clause, and, in particular,

[nothing in the said sub-clause shall affect the operation of any existing law in so far as it relates to, or
prevent the State from making any law relating to,—
<br>(i) the professional or technical qualifications necessary for practising any profession or carrying on
any occupation, trade or business, or
<br>(ii) the carrying on by the State, or by a corporation owned or controlled by the State, of any trade,
business, industry or service, whether to the exclusion, complete or partial, of citizens or otherwise].
""",




""" <b>Protection in respect of conviction for offences </b><br>(1) No person shall be convicted of any offence
except for violation of a law in force at the time of the commission of the Act charged as an offence, nor be
subjected to a penalty greater than that which might have been inflicted under the law in force at the time of
the commission of the offence.
<br>(2) No person shall be prosecuted and punished for the same offence more than once.
<br>(3) No person accused of any offence shall be compelled to be a witness against himself""",
""" <b> Protection of life and personal liberty</b>—No person shall be deprived of his life or personal liberty
except according to procedure established by law.
3
[21A. Right to education.—The State shall provide free and compulsory education to all children of
the age of six to fourteen years in such manner as the State may, by law, determine.]
""",
""" <b>Protection against arrest and detention in certain cases.— </b><br>(1) No person who is arrested shall be
detained in custody without being informed, as soon as may be, of the grounds for such arrest nor shall he be
denied the right to consult, and to be defended by, a legal practitioner of his choice.
<br>(2) Every person who is arrested and detained in custody shall be produced before the nearest magistrate
within a period of twenty-four hours of such arrest excluding the time necessary for the journey from the
place of arrest to the court of the magistrate and no such person shall be detained in custody beyond the said
period without the authority of a magistrate.
<br>(3) Nothing in clauses (1) and (2) shall apply—
(a) to any person who for the time being is an enemy alien; or
(b) to any person who is arrested or detained under any law providing for preventive detention.

<br>(4) No law providing for preventive detention shall authorise the detention of a person for a longer
period than three months unless (a) an Advisory Board consisting of persons who are, or have been, or are qualified to be appointed
as, Judges of a High Court has reported before the expiration of the said period of three months that
there is in its opinion sufficient cause for such detention:
Provided that nothing in this sub-clause shall authorise the detention of any person beyond the
maximum period prescribed by any law made by Parliament under sub-clause (b) of clause (7); or
(b) such person is detained in accordance with the provisions of any law made by Parliament under
sub-clauses (a) and (b) of clause (7).
<br>(5) When any person is detained in pursuance of an order made under any law providing for preventive
detention, the authority making the order shall, as soon as may be, communicate to such person the grounds
on which the order has been made and shall afford him the earliest opportunity of making a representation
against the order.
<br>(6) Nothing in clause (5) shall require the authority making any such order as is referred to in that clause
to disclose facts which such authority considers to be against the public interest to disclose.
<br>(7) Parliament may by law prescribe—
[(a) the circumstances under which, and the class or classes of cases in which, a person may be
detained for a period longer than three months under any law providing for preventive detention without
obtaining the opinion of an Advisory Board in accordance with the provisions of sub-clause (a) of clause
(4)];
(b) the maximum period for which any person may in any class or classes of cases be detained
under any law providing for preventive detention; and
***(c) the procedure to be followed by an Advisory Board in an inquiry under **
[sub-clause (a) of
clause (4)].

""",
""" <b> Prohibition of traffic in human beings and forced labour.</b><br>(1) Traffic in human beings and
begar and other similar forms of forced labour are prohibited and any contravention of this provision shall
be an offence punishable in accordance with law.
<br>(2) Nothing in this article shall prevent the State from imposing compulsory service for public purposes,
and in imposing such service the State shall not make any discrimination on grounds only of religion, race,
caste or class or any of them.""",
""" <b>. Prohibition of employment of children in factories </b>No child below the age of fourteen
years shall be employed to work in any factory or mine or engaged in any other hazardous employment.""",
""" <b>. Freedom of conscience and free profession, practice and propagation of religion.— </b><br>(1) Subject to
public order, morality and health and to the other provisions of this Part, all persons are equally entitled to
freedom of conscience and the right freely to profess, practise and propagate religion.
<br>(2) Nothing in this article shall affect the operation of any existing law or prevent the State from making
any law—
(a) regulating or restricting any economic, financial, political or other secular activity which may be
associated with religious practice;(b) providing for social welfare and reform or the throwing open of Hindu religious institutions of a
public character to all classes and sections of Hindus.
Explanation I.—The wearing and carrying of kirpans shall be deemed to be included in the profession of
the Sikh religion.
Explanation II.—In sub-clause (b) of clause (2), the reference to Hindus shall be construed as including a
reference to persons professing the Sikh, Jaina or Buddhist religion, and the reference to Hindu religious
institutions shall be construed accordingly.
""",
""" <b> Freedom to manage religious affairs.—</b>Subject to public order, morality and health, every religious
denomination or any section thereof shall have the right—
<br>(a) to establish and maintain institutions for religious and charitable purposes;
<br>(b) to manage its own affairs in matters of religion;
<br>(c) to own and acquire movable and immovable property; and
<br>(d) to administer such property in accordance with law.
""",
""" <b> Freedom as to payment of taxes for promotion of any particular religion.</b>No person shall be
compelled to pay any taxes, the proceeds of which are specifically appropriated in payment of expenses for
the promotion or maintenance of any particular religion or religious denomination.""",
""" <b>  Freedom as to attendance at religious instruction or religious worship in certain educational
institutions.</b><br>(1) No religious instruction shall be provided in any educational institution wholly maintained
out of State funds.
<br>(2) Nothing in clause (1) shall apply to an educational institution which is administered by the State but
has been established under any endowment or trust which requires that religious instruction shall be
imparted in such institution.
<br>(3) No person attending any educational institution recognised by the State or receiving aid out of State
funds shall be required to take part in any religious instruction that may be imparted in such institution or to
attend any religious worship that may be conducted in such institution or in any premises attached thereto
unless such person or, if such person is a minor, his guardian has given his consent thereto.""",
""" <b>Protection of interests of minorities. </b><br>(1) Any section of the citizens residing in the territory of
India or any part thereof having a distinct language, script or culture of its own shall have the right to
conserve the same.
<br>(2) No citizen shall be denied admission into any educational institution maintained by the State or
receiving aid out of State funds on grounds only of religion, race, caste, language or any of them.""",




""" <b>  Right of minorities to establish and administer educational institutions</b><br>(1) All minorities,
whether based on religion or language, shall have the right to establish and administer educational
institutions of their choice.

<br>[(1A) In making any law providing for the compulsory acquisition of any property of an educational
institution established and administered by a minority, referred to in clause (1), the State shall ensure that the
amount fixed by or determined under such law for the acquisition of such property is such as would not
restrict or abrogate the right guaranteed under that clause.]
<br>(2) The State shall not, in granting aid to educational institutions, discriminate against any educational institution on the ground that it is under the management of a minority, whether based on religion or
language.
""",
  """ 1. <b>[Compulsory acquisition of property.]—Omitted by the Constitution (Forty-fourth Amendment) Act,
1978, s. 6 (w.e.f. 20-6-1979).
[Saving of Certain Laws]
[31A. Saving of laws providing for acquisition of estates, etc.</b>

<br>[(1) Notwithstanding anything
contained in article 13, no law providing for—
<br>(a) the acquisition by the State of any estate or of any rights therein or the extinguishment or
modification of any such rights, or
<br>(b) the taking over of the management of any property by the State for a limited period either in the
public interest or in order to secure the proper management of the property, or
<br>(c) the amalgamation of two or more corporations either in the public interest or in order to secure
the proper management of any of the corporations, or
<br>(d) the extinguishment or modification of any rights of managing agents, secretaries and treasurers,
managing directors, directors or managers of corporations, or of any voting rights of shareholders
thereof, or
<br>(e) the extinguishment or modification of any rights accruing by virtue of any agreement, lease or
licence for the purpose of searching for, or winning, any mineral or mineral oil, or the premature
termination or cancellation of any such agreement, lease or licence,
shall be deemed to be void on the ground that it is inconsistent with, or takes away or abridges any of the
rights conferred by 5
[article 14 or article 19]:
Provided that where such law is a law made by the Legislature of a State, the provisions of this article
shall not apply thereto unless such law, having been reserved for the consideration of the President, has
received his assent:]
[Provided further that where any law makes any provision for the acquisition by the State of any estate
and where any land comprised therein is held by a person under his personal cultivation, it shall not be
lawful for the State to acquire any portion of such land as is within the ceiling limit applicable to him under
any law for the time being in force or any building or structure standing thereon or appurtenant thereto,
unless the law relating to the acquisition of such land, building or structure, provides for payment of
compensation at a rate which shall not be less than the market value thereof.]
<br>(2) In this article,—
<br>[(a) the expression ―estate‖ shall, in relation to any local area, have the same meaning as that expression
or its local equivalent has in the existing law relating to land tenures in force in that area and shall also
include<br>(i) any jagir, inam or muafi or other similar grant and in the States of 1
[Tamil Nadu] and Kerala,
any janmam right;
<br>(ii) any land held under ryotwari settlement;
<br>(iii) any land held or let for purposes of agriculture or for purposes ancillary thereto, including
waste land, forest land, land for pasture or sites of buildings and other structures occupied by
cultivators of land, agricultural labourers and village artisans;]
<br>(b) the expression ―rights‖, in relation to an estate, shall include any rights vesting in a proprietor,
sub-proprietor, under-proprietor, tenure-holder, 2
[raiyat, under-raiyat] or other intermediary and any
rights or privileges in respect of land revenue.]
<b>[31B. Validation of certain Acts and Regulations.</b>—Without prejudice to the generality of the
provisions contained in article 31A, none of the Acts and Regulations specified in the Ninth Schedule nor
any of the provisions thereof shall be deemed to be void, or ever to have become void, on the ground that
such Act, Regulation or provision is inconsistent with, or takes away or abridges any of the rights conferred
by, any provisions of this Part, and notwithstanding any judgment, decree or order of any court or Tribunal
to the contrary, each of the said Acts and Regulations shall, subject to the power of any competent
Legislature to repeal or amend it, continue in force.]
<b>[31C. Saving of laws giving effect to certain directive principles.</b>—Notwithstanding anything
contained in article 13, no law giving effect to the policy of the State towards securing 5
[all or any of the
principles laid down in Part IV] shall be deemed to be void on the ground that it is inconsistent with, or takes
away or abridges any of the rights conferred by 6
[article 14 or article 19]; 7
[and no law containing a
declaration that it is for giving effect to such policy shall be called in question in any court on the ground
that it does not give effect to such policy]:
Provided that where such law is made by the Legislature of a State, the provisions of this article shall not
apply thereto unless such law, having been reserved for the consideration of the President, has received his
assent.]
<b>31D. [Saving of laws in respect of anti-national activities.].</b>–Omitted by the Constitution (Forty-third
Amendment) Act, 1977, s. 2 (w.e.f. 13-4-1978).

""",
""" <b> Remedies for enforcement of rights conferred by this Part.</b><br>(1) The right to move the Supreme
Court by appropriate proceedings for the enforcement of the rights conferred by this Part is guaranteed.
<br>(2) The Supreme Court shall have power to issue directions or orders or writs, including writs in the
nature of habeas corpus, mandamus, prohibition, quo warranto and certiorari, whichever may be
appropriate, for the enforcement of any of the rights conferred by this Part.
<br>(3) Without prejudice to the powers conferred on the Supreme Court by clauses (1) and (2), Parliament may by law empower any other court to exercise within the local limits of its jurisdiction all or any of the
powers exercisable by the Supreme Court under clause (2).
<br>(4) The right guaranteed by this article shall not be suspended except as otherwise provided for by this
Constitution.
<br>[32A.Constitutional validity of State laws not to be considered in proceedings under article 32.].–
Omitted by the Constitution (Forty-third Amendment) Act, 1977, s. 3 (w.e.f. 13-4-1978). """,
""" <b>
[33. Power of Parliament to modify the rights conferred by this Part in their application to Forces,
etc </b>—Parliament may, by law, determine to what extent any of the rights conferred by this Part shall, in their
application to,—
<br>(a) the members of the Armed Forces; or
<br>(b) the members of the Forces charged with the maintenance of public order; or
<br>(c) persons employed in any bureau or other organisation established by the State for purposes of
intelligence or counter intelligence; or
<br>(d) person employed in, or in connection with, the telecommunication systems set up for the
purposes of any Force, bureau or organisation referred to in clauses (a) to (c),
be restricted or abrogated so as to ensure the proper discharge of their duties and the maintenance of
discipline among them.]""",
""" <b>Restriction on rights conferred by this Part while martial law is in force in any area. </b>Notwithstanding anything in the foregoing provisions of this Part, Parliament may by law indemnify any
person in the service of the Union or of a State or any other person in respect of any act done by him in
connection with the maintenance or restoration of order in any area within the territory of India where
martial law was in force or validate any sentence passed, punishment inflicted, forfeiture ordered or other act
done under martial law in such area.
""",
""" <b> Legislation to give effect to the provisions of this Part. </b>—Notwithstanding anything in this
Constitution,—
<br>(a) Parliament shall have, and the Legislature of a State shall not have, power to make laws—
<br>(i) with respect to any of the matters which under clause (3) of article 16, clause (3) of article 32,
article 33 and article 34 may be provided for by law made by Parliament; and
<br>(ii) for prescribing punishment for those acts which are declared to be offences under this Part,
and Parliament shall, as soon as may be after the commencement of this Constitution, make laws for
prescribing punishment for the acts referred to in sub-clause (ii);
<br>(b) any law in force immediately before the commencement of this Constitution in the territory of
India with respect to any of the matters referred to in sub-clause (i) of clause (a) or providing for
punishment for any act referred to in sub-clause (ii) of that clause shall, subject to the terms thereof and
to any adaptations and modifications that may be made therein under article 372, continue in force until
altered or repealed or amended by Parliament.
Explanation.—In this article, the expression ―law in force‖ has the same meaning as in article 372. """,
""" <b>Definition. </b>In this Part, unless the context otherwise requires, ―the State‖ has the same meaning as
in Part III.""",
""" <br> Application of the principles contained in this Part.—</b>The provisions contained in this Part shall
not be enforceable by any court, but the principles therein laid down are nevertheless fundamental in the
governance of the country and it shall be the duty of the State to apply these principles in making laws.""",
""" <b>. State to secure a social order for the promotion of welfare of the people.— </b><br>[(1)] The State shall
strive to promote the welfare of the people by securing and protecting as effectively as it may a social order in
which justice, social, economic and political, shall inform all the institutions of the national life.
<br>[(2) The State shall, in particular, strive to minimise the inequalities in income, and endeavour to
eliminate inequalities in status, facilities and opportunities, not only amongst individuals but also amongst
groups of people residing in different areas or engaged in different vocations.]
""",
""" <b>. Certain principles of policy to be followed by the State.— </b>—The State shall, in particular, direct its
policy towards securing—
<br>(a) that the citizens, men and women equally, have the right to an adequate means of livelihood;
(b)that the ownership and control of the material resources of the community are so distributed as
best to subserve the common good;
<br>(c) that the operation of the economic system does not result in the concentration of wealth and
means of production to the common detriment;
<br>(d) that there is equal pay for equal work for both men and women;
<br>(e) that the health and strength of workers, men and women, and the tender age of children are not
abused and that citizens are not forced by economic necessity to enter avocations unsuited to their age or
strength;
<br>[(f) that children are given opportunities and facilities to develop in a healthy manner and in
conditions of freedom and dignity and that childhood and youth are protected against exploitation and
against moral and material abandonment.]
[<br><b>39A. Equal justice and free legal aid.</b>—The State shall secure that the operation of the legal system
promotes justice, on a basis of equal opportunity, and shall, in particular, provide free legal aid, by suitable
legislation or schemes or in any other way, to ensure that opportunities for securing justice are not denied to
any citizen by reason of economic or other disabilities.]""",
""" <b> . Organisation of village panchayats.</b>—The State shall take steps to organise village panchayats and endow them with such powers and authority as may be necessary to enable them to function as units of
self-government.""",




""" <b>Right to work, to education and to public assistance in certain cases </b>The State shall, within the
limits of its economic capacity and development, make effective provision for securing the right to work, to
education and to public assistance in cases of unemployment, old age, sickness and disablement, and in other
cases of undeserved want.""",
""" <b>Provision for just and humane conditions of work and maternity relief. </b>The State shall make
provision for securing just and humane conditions of work and for maternity relief.""",
""" <b>Living wage, etc., for workers.—The State shall endeavour to secure, by suitable legislation or
economic organisation or in any other way, to all workers, agricultural, industrial or otherwise, work, a
living wage, conditions of work ensuring a decent standard of life and full enjoyment of leisure and social
and cultural opportunities and, in particular, the State shall endeavour to promote cottage industries on an
individual or co-operative basis in rural areas.

[43A. Participation of workers in management of industries.—The State shall take steps, by suitable
legislation or in any other way, to secure the participation of workers in the management of undertakings,
establishments or other organisations engaged in any industry.]
[43B. Promotion of co-operative societies.—The State shall endeavour to promote voluntary
formation, autonomous functioning, democratic control and professional management of co-operative
societies.]""",
""" <b>Uniform civil code for the citizens. </b>The State shall endeavour to secure for the citizens a uniform
civil code throughout the territory of India.
""",
""" <b>Provision for early childhood care and education to children below the age of six years. </b> The
State shall endeavour to provide early childhood care and education for all children until they complete the
age of six years.]""",
""" <b>Promotion of educational and economic interests of Scheduled Castes, Scheduled Tribes and
other weaker sections. </b>—The State shall promote with special care the educational and economic interests
of the weaker sections of the people, and, in particular, of the Scheduled Castes and the Scheduled Tribes,
and shall protect them from social injustice and all forms of exploitation.""",
""" <b>Duty of the State to raise the level of nutrition and the standard of living and to improve public
health. </b>The State shall regard the raising of the level of nutrition and the standard of living of its people
and the improvement of public health as among its primary duties and, in particular, the State shall
endeavour to bring about prohibition of the consumption except for medicinal purposes of intoxicating
drinks and of drugs which are injurious to health.""",
""" <b>Organisation of agriculture and animal husbandry. </b>The State shall endeavour to organise
agriculture and animal husbandry on modern and scientific lines and shall, in particular, take steps for
preserving and improving the breeds, and prohibiting the slaughter, of cows and calves and other milch and
draught cattle.
<br>[48A. Protection and improvement of environment and safeguarding of forests and wild life.—
The State shall endeavour to protect and improve the environment and to safeguard the forests and wild life
of the country.]""",
""" <b>Protection of monuments and places and objects of national importance.</b>It shall be the
obligation of the State to protect every monument or place or object of artistic or historic interest, 2
[declared
by or under law made by Parliament] to be of national importance, from spoliation, disfigurement,
destruction, removal, disposal or export, as the case may be.""",
""" <b>Separation of judiciary from executive </b>The State shall take steps to separate the judiciary from
the executive in the public services of the State.""",




""" <b> . Promotion of international peace and security.</b>The State shall endeavour to—
<br>(a) promote international peace and security;
<br>(b) maintain just and honourable relations between nations;
<br>(c) foster respect for international law and treaty obligations in the dealings of organised peoples
with one another; and
<br>(d) encourage settlement of international disputes by arbitration.
 <b> 51A. Fundamental duties.</b><br>It shall be the duty of every citizen of India—
<br>(a) to abide by the Constitution and respect its ideals and institutions, the National Flag and the
National Anthem;
<br>(b) to cherish and follow the noble ideals which inspired our national struggle for freedom;
<br>(c) to uphold and protect the sovereignty, unity and integrity of India;
<br>(d) to defend the country and render national service when called upon to do so;
<br>(e) to promote harmony and the spirit of common brotherhood amongst all the people of India
transcending religious, linguistic and regional or sectional diversities; to renounce practices derogatory
to the dignity of women;
<br>(f) to value and preserve the rich heritage of our composite culture;
<br>(g) to protect and improve the natural environment including forests, lakes, rivers and wild life, and
to have compassion for living creatures;
<br>(h) to develop the scientific temper, humanism and the spirit of inquiry and reform;
<br>(i) to safeguard public property and to abjure violence;
<br>(j) to strive towards excellence in all spheres of individual and collective activity so that the nation
constantly rises to higher levels of endeavour and achievement;
<br>[(k) who is a parent or guardian to provide opportunities for education to his child or, as the case
may be, ward between the age of six and fourteen years.]
""",
""" <b>  The President of India.</b>There shall be a President of India.""",
""" <b> Executive power of the Union.</b><br>(1) The executive power of the Union shall be vested in the President
and shall be exercised by him either directly or through officers subordinate to him in accordance with this
Constitution.
(2) Without prejudice to the generality of the foregoing provision, the supreme command of the Defence
Forces of the Union shall be vested in the President and the exercise thereof shall be regulated by law.
(3) Nothing in this article shall—
(a) be deemed to transfer to the President any functions conferred by any existing law on the
Government of any State or other authority; or
(b) prevent Parliament from conferring by law functions on authorities other than the President.""",
""" <b> Election of President.</b>The President shall be elected by the members of an electoral college
consisting of—
<br>(a) the elected members of both Houses of Parliament; and
<br>(b) the elected members of the Legislative Assemblies of the States.
<br>[Explanation.—In this article and in article 55, ―State‖ includes the National Capital Territory of
Delhi and the Union territory of *Pondicherry.]""",
""" <b> Manner of election of President.</b><br>(1) As far as practicable, there shall be uniformity in the scale of
representation of the different States at the election of the President.
<br>(2) For the purpose of securing such uniformity among the States inter se as well as parity between the
States as a whole and the Union, the number of votes which each elected member of Parliament and of the
<b>Legislative Assembly of each State is entitled to cast at such election shall be determined in the following
manner:</b>
<br>(a) every elected member of the Legislative Assembly of a State shall have as many votes as there
are multiples of one thousand in the quotient obtained by dividing the population of the State by the total
number of the elected members of the Assembly;
<br>(b) if, after taking the said multiples of one thousand, the remainder is not less than five hundred,
then the vote of each member referred to in sub-clause (a) shall be further increased by one;
<br>(c) each elected member of either House of Parliament shall have such number of votes as may be
obtained by dividing the total number of votes assigned to the members of the Legislative Assemblies of
the States under sub-clauses (a) and (b)by the total number of the elected members of both Houses of
Parliament, fractions exceeding one-half being counted as one and other fractions being disregarded.
<br>(3) The election of the President shall be held in accordance with the system of proportional
representation by means of the single transferable vote and the voting at such election shall be by secret
ballot.
<br>[Explanation.—In this article, the expression ―population‖ means the population as ascertained at the
last preceding census of which the relevant figures have been published:
Provided that the reference in this Explanation to the last preceding census of which the relevant figures
have been published shall, until the relevant figures for the first census taken after the year 2
[2026 have been
published, be construed as a reference to the 1971 census.]""",
""" <b> Term of office of President.</b>(1) The President shall hold office for a term of five years from the
date on which he enters upon his office:
Provided that—
<br>(a) the President may, by writing under his hand addressed to the Vice-President, resign his office;
<br>(b) the President may, for violation of the Constitution, be removed from office by impeachment in
the manner provided in article 61;
<br>(c) the President shall, notwithstanding the expiration of his term, continue to hold office until his
successor enters upon his office.
(2) Any resignation addressed to the Vice-President under clause (a) of the proviso to clause (1) shall
forthwith be communicated by him to the Speaker of the House of the People.""",
""" <b>  Eligibility for re-election.</b>A person who holds, or who has held, office as President shall, subject
to the other provisions of this Constitution, be eligible for re-election to that office.""",
""" <b> Qualifications for election as President.</b><br>(1) No person shall be eligible for election as President
unless he—
<br>(a) is a citizen of India,
<br>(b) has completed the age of thirty-five years, and
<br>(c) is qualified for election as a member of the House of the People.
<br>(2) A person shall not be eligible for election as President if he holds any office of profit under the
Government of India or the Government of any State or under any local or other authority subject to the
control of any of the said Governments.
Explanation.—For the purposes of this article, a person shall not be deemed to hold any office of profit
by reason only that he is the President or Vice-President of the Union or the Governor3
*** of any State or is
a Minister either for the Union or for any State.""",
""" <b> Conditions of President's office</b><br>(1) The President shall not be a member of either House of
Parliament or of a House of the Legislature of any State, and if a member of either House of Parliament or of
a House of the Legislature of any State be elected President, he shall be deemed to have vacated his seat in
that House on the date on which he enters upon his office as President.
<br>(2) The President shall not hold any other office of profit.
<br>(3) The President shall be entitled without payment of rent to the use of his official residences and shall
be also entitled to such emoluments, allowances and privileges as may be determined by Parliament by law
and, until provision in that behalf is so made, such emoluments, allowances and privileges as are specified in
the Second Schedule.
<br>(4) The emoluments and allowances of the President shall not be diminished during his term of office.""",
""" <b> Oath or affirmation by the President.</b>Every President and every person acting as President or
discharging the functions of the President shall, before entering upon his office, make and subscribe in the
presence of the Chief Justice of India or, in his absence, the senior-most Judge of the Supreme Court
available, an oath or affirmation in the following form, that is to say—
―I, A.B., do swear in the name of God that I will faithfully execute the office
solemnly affirm
of President (or discharge the functions of the President) of India and will to the best of my ability preserve,
protect and defend the Constitution and the law and that I will devote myself to the service and wellbeing of the people of India.".
""",







""" <b>Procedure for impeachment of the President.</b><br>(1) When a President is to be impeached for
violation of the Constitution, the charge shall be preferred by either House of Parliament.
<br>(2) No such charge shall be preferred unless—
<br>(a) the proposal to prefer such charge is contained in a resolution which has been moved after at
least fourteen days' notice in writing signed by not less than one-fourth of the total number of members
of the House has been given of their intention to move the resolution, and
<br>(b) such resolution has been passed by a majority of not less than two-thirds of the total membership
of the House.
<br>(3) When a charge has been so preferred by either House of Parliament, the other House shall investigate
the charge or cause the charge to be investigated and the President shall have the right to appear and to be
represented at such investigation.
<br>(4) If as a result of the investigation a resolution is passed by a majority of not less than two-thirds of the
total membership of the House by which the charge was investigated or caused to be investigated, declaring
that the charge preferred against the President has been sustained, such resolution shall have the effect of
removing the President from his office as from the date on which the resolution is so passed.""",
""" <b>Time of holding election to fill vacancy in the office of President and the term of office of
person elected to fill casual vacancy.</b><br>(1) An election to fill a vacancy caused by the expiration of the
term of office of President shall be completed before the expiration of the term.
<br>(2) An election to fill a vacancy in the office of President occurring by reason of his death, resignation
or removal, or otherwise shall be held as soon as possible after, and in no case later than six months from,
the date of occurrence of the vacancy; and the person elected to fill the vacancy shall, subject to the
provisions of article 56, be entitled to hold office for the full term of five years from the date on which he enters upon his office.
<b> The Vice-President of India.</b><br>There shall be a Vice-President of India.""",
""" <b>The Vice-President to be ex officio Chairman of the Council of States.</b><br>The Vice-President shall
be ex officio Chairman of the Council of the States and shall not hold any other office of profit:
Provided that during any period when the Vice-President acts as President or discharges the functions of
the President under article 65, he shall not perform the duties of the office of Chairman of the Council of
States and shall not be entitled to any salary or allowance payable to the Chairman of the Council of States
under article 97.""",
""" <b>The Vice-President to act as President or to discharge his functions during casual
vacancies in the office, or during the absence, of President.</b><br>(1) In the event of the occurrence of
any vacancy in the office of the President by reason of his death, resignation or removal, or otherwise, the
Vice-President shall act as President until the date on which a new President elected in accordance with the
provisions of this Chapter to fill such vacancy enters upon his office.
<br>(2) When the President is unable to discharge his functions owing to absence, illness or any other cause,
the Vice-President shall discharge his functions until the date on which the President resumes his duties.
<br>(3) The Vice-President shall, during, and in respect of, the period while he is so acting as, or discharging
the functions of, President, have all the powers and immunities of the President and be entitled to such
emoluments, allowances and privileges as may be determined by Parliament by law and, until provision in
that behalf is so made, such emoluments, allowances and privileges as are specified in the Second Schedule.""",
""" <b>Election of Vice-President.</b><br>(1) The Vice-President shall be elected by the 1
[members of an
electoral college consisting of the members of both Houses of Parliament] in accordance with the system of
proportional representation by means of the single transferable vote and the voting at such election shall be
by secret ballot.
<br>(2) The Vice-President shall not be a member of either House of Parliament or of a House of the
Legislature of any State, and if a member of either House of Parliament or of a House of the Legislature of
any State be elected Vice-President, he shall be deemed to have vacated his seat in that House on the date on
which he enters upon his office as Vice-President.
<br>(3) No person shall be eligible for election as Vice-President unless he—
<br>(a) is a citizen of India;
<br>(b) has completed the age of thirty-five years; and
<br>(c) is qualified for election as a member of the Council of States.
<br>(4) A person shall not be eligible for election as Vice-President if he holds any office of profit under the
Government of India or the Government of any State or under any local or other authority subject to the
control of any of the said Governments.
Explanation.—For the purposes of this article, a person shall not be deemed to hold any office of profit
by reason only that he is the President or Vice-President of the Union or the Governor2
*** of any State or is
a Minister either for the Union or for any State.""",
""" <b> Term of office of Vice-President.</b><br>The Vice-President shall hold office for a term of five years from the date on which he enters upon his office:
Provided that—
<br>(a) a Vice-President may, by writing under his hand addressed to the President, resign his office;
<br>(b) a Vice-President may be removed from his office by a resolution of the Council of States passed
by a majority of all the then members of the Council and agreed to by the House of the People; but no
resolution for the purpose of this clause shall be moved unless at least fourteen days' notice has been
given of the intention to move the resolution;
<br>(c) a Vice-President shall, notwithstanding the expiration of his term, continue to hold office until
his successor enters upon his office.""",
""" <b>Time of holding election to fill vacancy in the office of Vice-President and the term of office of
person elected to fill casual vacancy.</b><br>(1) An election to fill a vacancy caused by the expiration of the
term of office of Vice-President shall be completed before the expiration of the term.
<br>(2) An election to fill a vacancy in the office of Vice-President occurring by reason of his death,
resignation or removal, or otherwise shall be held as soon as possible after the occurrence of the vacancy,
and the person elected to fill the vacancy shall, subject to the provisions of article 67, be entitled to hold
office for the full term of five years from the date on which he enters upon his office.""",
""" <b>Oath or affirmation by the Vice-President.</b><br>Every Vice-President shall, before entering upon his
office, make and subscribe before the President, or some person appointed in that behalf by him, an oath or
affirmation in the following form, that is to say—
 ―I, A.B., do swear in the name of Godthat I will bear true faith and
 solemnly affirm
allegiance to the Constitution of India as by law established and that I will faithfully discharge the duty upon
which I am about to enter.‖.""",
""" <b>Discharge of President's functions in other contingencies.</b><br>Parliament may make such
provisions as it thinks fit for the discharge of the functions of the President in any contingency not provided
for in this Chapter.""",






""" <b>Matters relating to, or connected with, the election of a President or Vice-President.</b><br>(1) All
doubts and disputes arising out of or in connection with the election of a President or Vice-President shall be
inquired into and decided by the Supreme Court whose decision shall be final.
<br>(2) If the election of a person as President or Vice-President is declared void by the Supreme Court, acts
done by him in the exercise and performance of the powers and duties of the office of President or VicePresident, as the case may be, on or before the date of the decision of the Supreme Court shall not be
invalidated by reason of that declaration.
<br>(3) Subject to the provisions of this Constitution, Parliament may by law regulate any matter relating to
or connected with the election of a President or Vice-President.
<br>(4) The election of a person as President or Vice-President shall not be called in question on the ground of the existence of any vacancy for whatever reason among the members of the electoral college electing
him.]""",
""" <b> Power of President to grant pardons, etc., and to suspend, remit or commute sentences in
certain cases.</b><br>(1) The President shall have the power to grant pardons, reprieves, respites or remissions of
punishment or to suspend, remit or commute the sentence of any person convicted of any offence—
<br>(a) in all cases where the punishment or sentence is by a Court Martial;
<br>(b) in all cases where the punishment or sentence is for an offence against any law relating to a
matter to which the executive power of the Union extends;
<br>(c) in all cases where the sentence is a sentence of death.
<br>(2) Nothing in sub-clause (a) of clause (1) shall affect the power conferred by law on any officer of the
Armed Forces of the Union to suspend, remit or commute a sentence passed by a Court Martial.
<br>(3) Nothing in sub-clause (c) of clause (1) shall affect the power to suspend, remit or commute a sentence
of death exercisable by the Governor
*** of a State under any law for the time being in force.""",
""" <b> Extent of executive power of the Union</b><br>(1) Subject to the provisions of this Constitution, the
executive power of the Union shall extend—
<br>(a) to the matters with respect to which Parliament has power to make laws; and
<br>(b) to the exercise of such rights, authority and jurisdiction as are exercisable by the Government of
India by virtue of any treaty or agreement:
Provided that the executive power referred to in sub-clause (a) shall not, save as expressly provided in
this Constitution or in any law made by Parliament, extend in any State2
*** to matters with respect to
which the Legislature of the State has also power to make laws.
<br>(2) Until otherwise provided by Parliament, a State and any officer or authority of a State may,
notwithstanding anything in this article, continue to exercise in matters with respect to which Parliament has
power to make laws for that State such executive power or functions as the State or officer or authority thereof
could exercise immediately before the commencement of this Constitution.
Council of Ministers""",
""" <b>Council of Ministers to aid and advise President.</b><br>[(1) There shall be a Council of Ministers with
the Prime Minister at the head to aid and advise the President who shall, in the exercise of his functions, act in
accordance with such advice:]
[Provided that the President may require the Council of Ministers to reconsider such advice, either
generally or otherwise, and the President shall act in accordance with the advice tendered after such
reconsideration.]
(2) The question whether any, and if so what, advice was tendered by Ministers to the President shall not
be inquired into in any court """,
""" <b> Other provisions as to Ministers.</b><br>(1) The Prime Minister shall be appointed by the President and
the other Ministers shall be appointed by the President on the advice of the Prime Minister.
<br>[(1A) The total number of Ministers, including the Prime Minister, in the Council of Ministers shall not
exceed fifteen per cent. of the total number of members of the House of the People.
<br>(1B) A member of either House of Parliament belonging to any political party who is disqualified for being
a member of that House under paragraph 2 of the Tenth Schedule shall also be disqualified to be appointed as a
Minister under clause (1) for duration of the period commencing from the date of his disqualification till the
date on which the term of his office as such member would expire or where he contests any election to either
House of Parliament before the expiry of such period, till the date on which he is declared elected, whichever is
earlier.]
<br>(2) The Ministers shall hold office during the pleasure of the President.
<br>(3) The Council of Ministers shall be collectively responsible to the House of the People.
<br>(4) Before a Minister enters upon his office, the President shall administer to him the oaths of office and of
secrecy according to the forms set out for the purpose in the Third Schedule.
<br>(5) A Minister who for any period of six consecutive months is not a member of either House of
Parliament shall at the expiration of that period cease to be a Minister.
<br>(6) The salaries and allowances of Ministers shall be such as Parliament may from time to time by law
determine and, until Parliament so determines, shall be as specified in the Second Schedule.
The Attorney-General for India""",
""" <b> Attorney-General for India.</b><br>(1) The President shall appoint a person who is qualified to be
appointed a Judge of the Supreme Court to be Attorney-General for India.
<br>(2) It shall be the duty of the Attorney-General to give advice to the Government of India upon such
legal matters, and to perform such other duties of a legal character, as may from time to time be referred or
assigned to him by the President, and to discharge the functions conferred on him by or under this
Constitution or any other law for the time being in force.
<br>(3) In the performance of his duties the Attorney-General shall have right of audience in all courts in the
territory of India.
<br>(4) The Attorney-General shall hold office during the pleasure of the President, and shall receive such
remuneration as the President may determine.
Conduct of Government Business""",
""" <b> Conduct of business of the Government of India.</b><br>(1) All executive action of the Government of
India shall be expressed to be taken in the name of the President.
 <br>(2) Orders and other instruments made and executed in the name of the President shall be authenticated
in such manner as may be specified in rules2
to be made by the President, and the validity of an order or  instrument which is so authenticated shall not be called in question on the ground that it is not an order or
instrument made or executed by the President.
 <br>(3) The President shall make rules for the more convenient transaction of the business of the
Government of India, and for the allocation among Ministers of the said business.""",

""" <b>Duties of Prime Minister as respects the furnishing of information to the President, etc.</b><br>It shall
be the duty of the Prime Minister—
<br>(a)to communicate to the President all decisions of the Council of Ministers relating to the
administration of the affairs of the Union and proposals for legislation;
<br>(b) to furnish such information relating to the administration of the affairs of the Union and
proposals for legislation as the President may call for; and
<br>(c)if the President so requires, to submit for the consideration of the Council of Ministers any matter
on which a decision has been taken by a Minister but which has not been considered by the Council.""",
""" <b>Constitution of Parliament.</b><br>There shall be a Parliament for the Union which shall consist of the
President and two Houses to be known respectively as the Council of States and the House of the People.""",
""" <b>Composition of the Council of States.<br>(1) [The Council of States] shall consist of—
<br>(a) twelve members to be nominated by the President in accordance with the provisions of
clause (3); and
<br>(b) not more than two hundred and thirty-eight representatives of the States 4
[and of the Union
territories.]
<br>(2) The allocation of seats in the Council of States to be filled by representatives of the States 4
[and of
the Union territories] shall be in accordance with the provisions in that behalf contained in the Fourth
Schedule.
<br>(3) The members to be nominated by the President under sub-clause (a) of clause (1) shall consist of persons having special knowledge or practical experience in respect of such matters as the following,
namely:—
Literature, science, art and social service.
<br>(4) The representatives of each State 1
 in the Council of States shall be elected by the elected
members of the Legislative Assembly of the State in accordance with the system of proportional
representation by means of the single transferable vote.
<br>(5) The representatives of the 2
[Union territories] in the Council of States shall be chosen in such manner
as Parliament may by law prescribe.""",




""" <b> Composition of the House of the People.</b><br>(1)
[Subject to the provisions of article 331 5
***],
the House of the People shall consist of—
<br>(a) not more than 6
[five hundred and thirty members] chosen by direct election from territorial
constituencies in the States, and
(b) not more than 7
[twenty members] to represent the Union territories, chosen in such manner as
Parliament may by law provide.
<br>(2) For the purposes of sub-clause (a) of clause (1),—
<br>(a) there shall be allotted to each State a number of seats in the House of the People in such manner
that the ratio between that number and the population of the State is, so far as practicable, the same for
all States; and
<br>(b) each State shall be divided into territorial constituencies in such manner that the ratio between
the population of each constituency and the number of seats allotted to it is, so far as practicable, the
same throughout the State:
<br>[Provided that the provisions of sub-clause (a)of this clause shall not be applicable for the purpose
of allotment of seats in the House of the People to any State so long as the population of that State does
not exceed six millions.]
<br>(3) In this article, the expression ―population‖ means the population as ascertained at the last preceding
census of which the relevant figures have been published:[Provided that the reference in this clause to the last preceding census of which the relevant figures have
been published shall, until the relevant figures for the first census taken after the year 2
[2026] have been
published, 3
[be construed,—
<br>(i) for the purposes of sub-clause (a) of clause (2) and the proviso to that clause, as a reference to the
1971 census; and
<br>(ii) for the purposes of sub-clause (b)of clause (2) as a reference to the 4
[2001] census.]""",

""" <b>Readjustment after each census.</b><br>Upon the completion of each census, the allocation of seats in
the House of the People to the States and the division of each State into territorial constituencies shall be
readjusted by such authority and in such manner as Parliament may by law determine:
Provided that such readjustment shall not affect representation in the House of the People until the
dissolution of the then existing House:
Provided further that such readjustment shall take effect from such date as the President may, by order,
specify and until such readjustment takes effect, any election to the House may be held on the basis of the
territorial constituencies existing before such readjustment:
Provided also that until the relevant figures for the first census taken after the year 5
[2026] have been
published, it shall not be necessary to 6
[readjust—
<br>(i) the allocation of seats in the House of the People to the States as readjusted on the basis of the
1971 census; and
<br>(ii) the division of each State into territorial constituencies as may be readjusted on the basis of the
[2001] census,
under this article.]""",

""" <b>Duration of Houses of Parliament</b><br>(1) The Council of States shall not be subject to dissolution,
but as nearly as possible one-third of the members thereof shall retire as soon as may be on the expiration of
every second year in accordance with the provisions made in that behalf by Parliament by law.
<br>(2) The House of the People, unless sooner dissolved, shall continue for 8
[five years] from the date
appointed for its first meeting and no longer and the expiration of the said period of 8
[five years] shall
operate as a dissolution of the House:
Provided that the said period may, while a Proclamation of Emergency is in operation, be extended by
Parliament by law for a period not exceeding one year at a time and not extending in any case beyond a
period of six months after the Proclamation has ceased to operate.
""",
""" <b> Qualification for membership of Parliament.</b><br>A person shall not be qualified to be chosen to fill
a seat in Parliament unless he—
<br>[(a) is a citizen of India, and makes and subscribes before some person authorised in that behalf by
the Election Commission an oath or affirmation according to the form set out for the purpose in the
Third Schedule;]
<br>(b) is, in the case of a seat in the Council of States, not less than thirty years of age and, in the case
of a seat in the House of the People, not less than twenty-five years of age; and
<br>(c) possesses such other qualifications as may be prescribed in that behalf by or under any law made
by Parliament.
""",
""" <b>Sessions of Parliament, prorogation and dissolution.</b><br>(1) The President shall from time to time
summon each House of Parliament to meet at such time and place as he thinks fit, but six months shall not
intervene between its last sitting in one session and the date appointed for its first sitting in the next session.
<br>(2) The President may from time to time—
<br>(a) prorogue the Houses or either House;
<br>(b) dissolve the House of the People.]""",

""" <b>Right of President to address and send messages to Houses.</b><br>(1) The President may address
either House of Parliament or both Houses assembled together, and for that purpose require the attendance of
members.""",
"""(2) The President may send messages to either House of Parliament, whether with respect to a Bill then
pending in Parliament or otherwise, and a House to which any message is so sent shall with all convenient
despatch consider any matter required by the message to be taken into consideration.
""",
""" <b>Special address by the President.</b><br>(1) At the commencement of 3
[the first session after each
general election to the House of the People and at the commencement of the first session of each year] the
President shall address both Houses of Parliament assembled together and inform Parliament of the causes of
its summons.
<br>(2) Provision shall be made by the rules regulating the procedure of either House for the allotment of
time for discussion of the matters referred to in such address4
***.""",

""" <b>Rights of Ministers and Attorney-General as respects Houses.</b><br>Every Minister and the
Attorney-General of India shall have the right to speak in, and otherwise to take part in the proceedings of,
either House, any joint sitting of the Houses, and any committee of Parliament of which he may be named a
member, but shall not by virtue of this article be entitled to vote.
Officers of Parliament""",

""" <b>The Chairman and Deputy Chairman of the Council of States.</b><br>(1) The Vice- President of India
shall be ex officio Chairman of the Council of States.
(2) The Council of States shall, as soon as may be, choose a member of the Council to be Deputy
Chairman thereof and, so often as the office of Deputy Chairman becomes vacant, the Council shall choose
another member to be Deputy Chairman thereof.""",

""" <b>Vacation and resignation of, and removal from, the office of Deputy Chairman.—A member
holding office as Deputy Chairman of the Council of States</b><br>
<br>(a) shall vacate his office if he ceases to be a member of the Council;
<br>(b) may at any time, by writing under his hand addressed to the Chairman, resign his office; and
<br>(c) may be removed from his office by a resolution of the Council passed by a majority of all the
then members of the Council:
Provided that no resolution for the purpose of clause (c)shall be moved unless at least fourteen days‘
notice has been given of the intention to move the resolution""",







""" <b> Power of the Deputy Chairman or other person to perform the duties of the office of, or to act
as, Chairman.</b><br>(1) While the office of Chairman is vacant, or during any period when theVice-President is
acting as, or discharging the functions of, President, the duties of the office shall be performed by the Deputy
Chairman, or, if the office of Deputy Chairman is also vacant, by such member of the Council of States as
the President may appoint for the purpose.
<br>(2)During the absence of the Chairman from any sitting of the Council of States the Deputy Chairman, or, if
he is also absent, such person as may be determined by the rules of procedure of the Council, or, if no such person
is present, such other person as may be determined by the Council, shall act as Chairman.""",
""" <b> The Chairman or the Deputy Chairman not to preside while a resolution for his removal from
office is under consideration.</b><br>(1) At any sitting of the Council of States, while any resolution for the
removal of the Vice-President from his office is under consideration, the Chairman, or while any resolution
for the removal of the Deputy Chairman from his office is under consideration, the Deputy Chairman, shall
not, though he is present, preside, and the provisions of clause (2) of article 91 shall apply in relation to
every such sitting as they apply in relation to a sitting from which the Chairman, or, as the case may be, the
Deputy Chairman, is absent.
<br>(2) The Chairman shall have the right to speak in, and otherwise to take part in the proceedings of, the
Council of States while any resolution for the removal of the Vice-President from his office is under
consideration in the Council, but, notwithstanding anything in article 100, shall not be entitled to vote at all
on such resolution or on any other matter during such proceedings.""",
""" <b>The Speaker and Deputy Speaker of the House of the People.</b><br>The House of the People shall, as
soon as may be, choose two members of the House to be respectively Speaker and Deputy Speaker thereof
and, so often as the office of Speaker or Deputy Speaker becomes vacant, the House shall choose another
member to be Speaker or Deputy Speaker, as the case may be.""",
""" <b> Vacation and resignation of, and removal from, the offices of Speaker and Deputy Speaker.—
A member holding office as Speaker or Deputy Speaker of the House of the People—
<br>(a) shall vacate his office if he ceases to be a member of the House of the People;
<br>(b) may at any time, by writing under his hand addressed, if such member is the Speaker, to the
Deputy Speaker, and if such member is the Deputy Speaker, to the Speaker, resign his office; and
<br>(c) may be removed from his office by a resolution of the House of the People passed by a majority
of all the then members of the House:
Provided that no resolution for the purpose of clause (c)shall be moved unless at least fourteen
days‘ notice has been given of the intention to move the resolution:
Provided further that, whenever the House of the People is dissolved, the Speaker shall not vacate
his office until immediately before the first meeting of the House of the People after the dissolution.""",
""" <b> Power of the Deputy Speaker or other person to perform the duties of the office of, or to act
as, Speaker.</b><br>(1) While the office of Speaker is vacant, the duties of the office shall be performed by the
Deputy Speaker or, if the office of Deputy Speaker is also vacant, by such member of the House of the
People as the President may appoint for the purpose.
<br>(2) During the absence of the Speaker from any sitting of the House of the People the Deputy Speaker or, if he
is also absent, such person as may be determined by the rules of procedure of the House, or, if no such person is
present, such other person as may be determined by the House, shall act as Speaker.""",
""" <b> The Speaker or the Deputy Speaker not to preside while a resolution for his removal from
office is under consideration</b><br>(1) At any sitting of the House of the People, while any resolution for the
removal of the Speaker from his office is under consideration, the Speaker, or while any resolution for the
removal of the Deputy Speaker from his office is under consideration, the Deputy Speaker, shall not, though
he is present, preside, and the provisions of clause (2) of article 95 shall apply in relation to every such
sitting as they apply in relation to a sitting from which the Speaker, or, as the case may be, the Deputy
Speaker, is absent.
<br>(2) The Speaker shall have the right to speak in, and otherwise to take part in the proceedings of, the
House of the People while any resolution for his removal from office is under consideration in the House and
shall, notwithstanding anything in article 100, be entitled to vote only in the first instance on such resolution
or on any other matter during such proceedings but not in the case of an equality of votes.""",
""" <b> Salaries and allowances of the Chairman and Deputy Chairman and the Speaker and Deputy
Speaker.</b><br>There shall be paid to the Chairman and the Deputy Chairman of the Council of States, and to
the Speaker and the Deputy Speaker of the House of the People, such salaries and allowances as may be
respectively fixed by Parliament by law and, until provision in that behalf is so made, such salaries and
allowances as are specified in the Second Schedule.""",
""" <b>Secretariat of Parliament.</b><br>(1) Each House of Parliament shall have a separate secretarial staff:
Provided that nothing in this clause shall be construed as preventing the creation of posts common to
both Houses of Parliament.
<br>(2) Parliament may by law regulate the recruitment, and the conditions of service of persons appointed,
to the secretarial staff of either House of Parliament.
<br>(3) Until provision is made by Parliament under clause (2), the President may, after consultation with the
Speaker of the House of the People or the Chairman of the Council of States, as the case may be, make rules
regulating the recruitment, and the conditions of service of persons appointed, to the secretarial staff of the
House of the People or the Council of States, and any rules so made shall have effect subject to the
provisions of any law made under the said clause.
<b> Conduct of Business
Oath or affirmation by members</b><br>Every member of either House of Parliament shall, before
taking his seat, make and subscribe before the President, or some person appointed in that behalf by him, an oath or affirmation according to the form set out for the purpose in the Third Schedule.""",
""" <b> Voting in Houses, power of Houses to act notwithstanding vacancies and quorum.</b><br>(1) Save
as otherwise provided in this Constitution, all questions at any sitting of either House or joint sitting of the
Houses shall be determined by a majority of votes of the members present and voting, other than the Speaker
or person acting as Chairman or Speaker.
The Chairman or Speaker, or person acting as such, shall not vote in the first instance, but shall have and
exercise a casting vote in the case of an equality of votes.
<br>(2) Either House of Parliament shall have power to act notwithstanding any vacancy in the membership
thereof, and any proceedings in Parliament shall be valid notwithstanding that it is discovered subsequently that
some person who was not entitled so to do sat or voted or otherwise took part in the proceedings.
<br>[(3) Until Parliament by law otherwise provides, the quorum to constitute a meeting of either House of
Parliament shall be one-tenth of the total number of members of the House.
<br>(4) If at any time during a meeting of a House there is no quorum, it shall be the duty of the Chairman or
Speaker, or person acting as such, either to adjourn the House or to suspend the meeting until there is a
quorum.]""",






""" <b> Vacation of seats.</b><br>(1) No person shall be a member of both Houses of Parliament and provision
shall be made by Parliament by law for the vacation by a person who is chosen a member of both Houses of
his seat in one House or the other.
<br>(2) No person shall be a member both of Parliament and of a House of the Legislature of a State2***, and
if a person is chosen a member both of Parliament and of a House of the Legislature of13
[a State], then, at the
expiration of such period as may be specified in rules4made by the President, that person‘s seat in Parliament
shall become vacant, unless he has previously resigned his seat in the Legislature of the State.
<br>(3) If a member of either House of Parliament—
<br>(a) becomes subject to any of the disqualifications mentioned in 5
[clause (1) or clause (2) of article
102], or

<br>[(b) resigns his seat by writing under his hand addressed to the Chairman or the Speaker, as the case
may be, and his resignation is accepted by the Chairman or the Speaker, as the case may be,]
his seat shall thereupon become vacant:

[Provided that in the case of any resignation referred to in sub-clause (b), if from information received or
otherwise and after making such inquiry as he thinks fit, the Chairman or the Speaker, as the case may be, is satisfied that such resignation is not voluntary or genuine, he shall not accept such resignation.]
<br>(4) If for a period of sixty days a member of either House of Parliament is without permission of the
House absent from all meetings thereof, the House may declare his seat vacant:
Provided that in computing the said period of sixty days no account shall be taken of any period during
which the House is prorogued or is adjourned for more than four consecutive days.""",
""" <b> Disqualifications for membership</b><br>(1) A person shall be disqualified for being chosen as, and
for being, a member of either House of Parliament—

<br>[(a) if he holds any office of profit under the Government of India or the Government of any State,
other than an office declared by Parliament by law not to disqualify its holder;]
(b) if he is of unsound mind and stands so declared by a competent court;
(c) if he is an undischarged insolvent;
(d) if he is not a citizen of India, or has voluntarily acquired the citizenship of a foreign State, oris
under any acknowledgment of allegiance or adherence to a foreign State;
(e) if he is so disqualified by or under any law made by Parliament.

<br>[Explanation.—For the purposes of this clause a person shall not be deemed to hold an office of profit
under the Government of India or the Government of any State by reason only that he is a Minister either for
the Union or for such State.]

<br>[(2) A person shall be disqualified for being a member of either House of Parliament if he is so
disqualified under the Tenth Schedule.]""",
""" <b> Decision on questions as to disqualifications of members.</b><br>(1) If any question arises as to
whether a member of either House of Parliament has become subject to any of the disqualifications
mentioned in clause (1) of article 102, the question shall be referred for the decision of the President and his
decision shall be final.
<br>(2) Before giving any decision on any such question, the President shall obtain the opinion of the
Election Commission and shall act according to such opinion.]""",
""" <b>Penalty for sitting and voting before making oath or affirmation under article 99 or when not
qualified or when disqualified.—If a person sits or votes as a member of either House of Parliament before
he has complied with the requirements of article 99, or when he knows that he is not qualified or that he is
disqualified for membership thereof, or that he is prohibited from so doing by the provisions of any law
made by Parliament, he shall be liable in respect of each day on which he so sits or votes to a penalty of five
hundred rupees to be recovered as a debt due to the Union.""",
""" <b>Powers, Privileges and Immunities of Parliament and its Members
Powers, privileges, etc., of the Houses of Parliament and of the members and committeesthereof.</b><br>(1) Subject to the provisions of this Constitution and to the rules and standing orders regulating
the procedure of Parliament, there shall be freedom of speech in Parliament.
(2) No member of Parliament shall be liable to any proceedings in any court in respect of anything said or any
vote given by him in Parliament or any committee thereof, and no person shall be so liable in respect of the
publication by or under the authority of either House of Parliament of any report, paper, votes or proceedings.
<br>[(3) In other respects, the powers, privileges and immunities of each House of Parliament, and of the
members and the committees of each House, shall be such as may from time to time be defined by
Parliament by law, and, until so defined, 2
[shall be those of that House and of its members and committees
immediately before the coming into force of section 15 of the Constitution (Forty-fourth Amendment) Act,
1978.]]
<br>(4) The provisions of clauses (1), (2) and (3) shall apply in relation to persons who by virtue of this
Constitution have the right to speak in, and otherwise to take part in the proceedings of, a House of
Parliament or any committee thereof as they apply in relation to members of Parliament.""",
""" <b> Salaries and allowances of members.</b><br>Members of either House of Parliament shall be entitled
to receive such salaries and allowances as may from time to time be determined by Parliament by law and,
until provision in that respect is so made, allowances at such rates and upon such conditions as were
immediately before the commencement of this Constitution applicable in the case of members of the
Constituent Assembly of the Dominion of India.
Legislative Procedure""",
""" <b>Provisions as to introduction and passing of Bills.</b><br>(1) Subject to the provisions of articles 109
and 117 with respect to Money Bills and other financial Bills, a Bill may originate in either House of
Parliament.
<br>(2) Subject to the provisions of articles 108 and 109, a Bill shall not be deemed to have been passed by
the Houses of Parliament unless it has been agreed to by both Houses, either without amendment or with
such amendments only as are agreed to by both Houses.
<br>(3) A Bill pending in Parliament shall not lapse by reason of the prorogation of the Houses.
<br>(4) A Bill pending in the Council of States which has not been passed by the House of the People shall
not lapse on a dissolution of the House of the People.
<br>(5) A Bill which is pending in the House of the People, or which having been passed by the House of the
People is pending in the Council of States, shall, subject to the provisions of article 108, lapse on a
dissolution of the House of the People.""",
""" <b> Joint sitting of both Houses in certain cases.</b><br>(1) If after a Bill has been passed by one House
and transmitted to the other House—
<br>(a) the Bill is rejected by the other House; or
<br>(b) the Houses have finally disagreed as to the amendments to be made in the Bill; or
<br>(c) more than six months elapse from the date of the reception of the Bill by the other House without
the Bill being passed by it,
the President may, unless the Bill has elapsed by reason of a dissolution of the House of the People, notify to the Houses by message if they are sitting or by public notification if they are not sitting, his intention to
summon them to meet in a joint sitting for the purpose of deliberating and voting on the Bill:
Provided that nothing in this clause shall apply to a Money Bill.
<br>(2) In reckoning any such period of six months as is referred to in clause (1), no account shall be taken
of any period during which the House referred to in sub-clause (c) of that clause is prorogued or adjourned
for more than four consecutive days.
<br>(3) Where the President has under clause (1) notified his intention of summoning the Houses to meet in a
joint sitting, neither House shall proceed further with the Bill, but the President may at any time after the date
of his notification summon the Houses to meet in a joint sitting for the purpose specified in the notification and,
if he does so, the Houses shall meet accordingly.
<br>(4) If at the joint sitting of the two Houses the Bill, with such amendments, if any, as are agreed to in joint
sitting, is passed by a majority of the total number of members of both Houses present and voting, it shall be
deemed for the purposes of this Constitution to have been passed by both Houses:
Provided that at a joint sitting—
<br>(a) if the Bill, having been passed by one House, has not been passed by the other House with
amendments and returned to the House in which it originated, no amendment shall be proposed to the
Bill other than such amendments (if any) as are made necessary by the delay in the passage of the Bill;
<br>(b) if the Bill has been so passed and returned, only such amendments as aforesaid shall be proposed to
the Bill and such other amendments as are relevant to the matters with respect to which the Houses have not
agreed;
and the decision of the person presiding as to the amendments which are admissible under this clause shall be final.
<br>(5) A joint sitting may be held under this article and a Bill passed thereat, notwithstanding that a
dissolution of the House of the People has intervened since the President notified his intention to summon
the Houses to meet therein.""",
""" <b>Special procedure in respect of Money Bills.</b><br>(1) A Money Bill shall not be introduced in the
Council of States.
<br>(2) After a Money Bill has been passed by the House of the People it shall be transmitted to the Council
of States for its recommendations and the Council of States shall within a period of fourteen days from the
date of its receipt of the Bill return the Bill to the House of the People with its recommendations and the
House of the People may thereupon either accept or reject all or any of the recommendations of the Council
of States.
<br>(3) If the House of the People accepts any of the recommendations of the Council of States, the Money
Bill shall be deemed to have been passed by both Houses with the amendments recommended by the
Council of States and accepted by the House of the People.
<br>(4) If the House of the People does not accept any of the recommendations of the Council of States, the
Money Bill shall be deemed to have been passed by both Houses in the form in which it was passed by the
House of the People without any of the amendments recommended by the Council of States.
<br>(5) If a Money Bill passed by the House of the People and transmitted to the Council of States for its
recommendations is not returned to the House of the People within the said period of fourteen days, it shall
be deemed to have been passed by both Houses at the expiration of the said period in the form in which it
was passed by the House of the People.""",
""" <b> Definition of ―Money Bills‖.</b><br>(1) For the purposes of this Chapter, a Bill shall be deemed to be a
Money Bill if it contains only provisions dealing with all or any of the following matters, namely:—(a) the imposition, abolition, remission, alteration or regulation of any tax;
<br>(b) the regulation of the borrowing of money or the giving of any guarantee by the Government of
India, or the amendment of the law with respect to any financial obligations undertaken or to be
undertaken by the Government of India;
<br>(c) the custody of the Consolidated Fund or the Contingency Fund of India, the payment of moneys
into or the withdrawal of moneys from any such Fund;
<br>(d) the appropriation of moneys out of the Consolidated Fund of India;
<br>(e) the declaring of any expenditure to be expenditure charged on the Consolidated Fund of India or
the increasing of the amount of any such expenditure;
<br>(f) the receipt of money on account of the Consolidated Fund of India or the public account of India
or the custody or issue of such money or the audit of the accounts of the Union or of a State; or
<br>(g) any matter incidental to any of the matters specified in sub-clauses (a) to (f).
<br>(2) A Bill shall not be deemed to be a Money Bill by reason only that it provides for the imposition of
fines or other pecuniary penalties, or for the demand or payment of fees for licences or fees for services
rendered, or by reason that it provides for the imposition, abolition, remission, alteration or regulation of any
tax by any local authority or body for local purposes.
<br>(3) If any question arises whether a Bill is a Money Bill or not, the decision of the Speaker of the House
of the People thereon shall be final.
<br>(4) There shall be endorsed on every Money Bill when it is transmitted to the Council of States under
article 109, and when it is presented to the President for assent under article 111, the certificate of the
Speaker of the House of the People signed by him that it is a Money Bill.""",








""" <b>Assent to Bills.</b><br>When a Bill has been passed by the Houses of Parliament, it shall be presented to
the President, and the President shall declare either that he assents to the Bill, or that he withholds assent
therefrom:
Provided that the President may, as soon as possible after the presentation to him of a Bill for assent,
return the Bill if it is not a Money Bill to the Houses with a message requesting that they will reconsider the
Bill or any specified provisions thereof and, in particular, will consider the desirability of introducing any
such amendments as he may recommend in his message, and when a Bill is so returned, the Houses shall
reconsider the Bill accordingly, and if the Bill is passed again by the Houses with or without amendment and
presented to the President for assent, the President shall not withhold assent therefrom.""",
""" <b>Procedure in Financial Matters

 <br>Annual financial statement.</b><br>(1) The President shall in respect of every financial year cause to be
laid before both the Houses of Parliament a statement of the estimated receipts and expenditure of the
Government of India for that year, in this Part referred to as the ―annual financial statement‖.
<br>(2) The estimates of expenditure embodied in the annual financial statement shall show separately—
<br>(a) the sums required to meet expenditure described by this Constitution as expenditure charged
upon the Consolidated Fund of India; and
<br>(b) the sums required to meet other expenditure proposed to be made from the Consolidated Fund of
India,
and shall distinguish expenditure on revenue account from other expenditure.
<br>(3) The following expenditure shall be expenditure charged on the Consolidated Fund of India—
<br>(a) the emoluments and allowances of the President and other expenditure relating to his office;
<br>(b) the salaries and allowances of the Chairman and the Deputy Chairman of the Council of States
and the Speaker and the Deputy Speaker of the House of the People;
<br>(c) debt charges for which the Government of India is liable including interest, sinking fund charges
and redemption charges, and other expenditure relating to the raising of loans and the service and
redemption of debt;
<br>(d) (i) the salaries, allowances and pensions payable to or in respect of Judges of the Supreme Court;
<br>(ii) the pensions payable to or in respect of Judges of the Federal Court;
<br>(iii) the pensions payable to or in respect of Judges of any High Court which exercises jurisdiction in
relation to any area included in the territory of India or which at any time before the commencement of
this Constitution exercised jurisdiction in relation to any area included in 1
[a Governor's Province of the
Dominion of India];
<br>(e) the salary, allowances and pension payable to or in respect of the Comptroller and AuditorGeneral of India;
<br>(f) any sums required to satisfy any judgment, decree or award of any court or arbitral tribunal;
<br>(g) any other expenditure declared by this Constitution or by Parliament by law to be so charged.""",
""" <b> Procedure in Parliament with respect to estimates.</b><br>(1) So much of the estimates as relates to
expenditure charged upon the Consolidated Fund of India shall not be submitted to the vote of Parliament,
but nothing in this clause shall be construed as preventing the discussion in either House of Parliament of
any of those estimates.
(2) So much of the said estimates as relates to other expenditure shall be submitted in the form of
demands for grants to the House of the People, and the House of the People shall have power to assent, or to
refuse to assent, to any demand, or to assent to any demand subject to a reduction of the amount specified
therein.
<br>(3) No demand for a grant shall be made except on the recommendation of the President.""",
""" <b> Appropriation Bills.</b><br>(1) As soon as may be after the grants under article 113 have been made by
the House of the People, there shall be introduced a Bill to provide for the appropriation out of the
Consolidated Fund of India of all moneys required to meet—
<br>(a) the grants so made by the House of the People; and
<br>(b) the expenditure charged on the Consolidated Fund of India but not exceeding in any case the
amount shown in the statement previously laid before Parliament.
<br>(2) No amendment shall be proposed to any such Bill in either House of Parliament which will have the
effect of varying the amount or altering the destination of any grant so made or of varying the amount of any
expenditure charged on the Consolidated Fund of India, and the decision of the person presiding as to
whether an amendment is inadmissible under this clause shall be final.
<br>(3) Subject to the provisions of articles 115 and 116, no money shall be withdrawn from the
Consolidated Fund of India except under appropriation made by law passed in accordance with the
provisions of this article.""",
""" <b> Supplementary, additional or excess grants.</b><br>(1) The President shall—
 <br>(a) if the amount authorised by any law made in accordance with the provisions of article 114 to
be expended for a particular service for the current financial year is found to be insufficient for the
purposes of that year or when a need has arisen during the current financial year for supplementary or additional expenditure upon some new service not contemplated in the annual financial statement for
that year, or
 <br>(b) if any money has been spent on any service during a financial year in excess of the amount
granted for that service and for that year,
cause to be laid before both the Houses of Parliament another statement showing the estimated amount of
that expenditure or cause to be presented to the House of the People a demand for such excess, as the case
may be.
<br>(2) The provisions of articles 112, 113 and 114 shall have effect in relation to any such statement and
expenditure or demand and also to any law to be made authorising the appropriation of moneys out of the
Consolidated Fund of India to meet such expenditure or the grant in respect of such demand as they have
effect in relation to the annual financial statement and the expenditure mentioned therein or to a demand for
a grant and the law to be made for the authorisation of appropriation of moneys out of the Consolidated Fund
of India to meet such expenditure or grant.""",
""" <b> Votes on account, votes of credit and exceptional grants.</b><br>(1) Notwithstanding anything in the
foregoing provisions of this Chapter, the House of the People shall have power—
<br>(a) to make any grant in advance in respect of the estimated expenditure for a part of any financial
year pending the completion of the procedure prescribed in article 113 for the voting of such grant and
the passing of the law in accordance with the provisions of article 114 in relation to that expenditure;
<br>(b) to make a grant for meeting an unexpected demand upon the resources of India when on account
of the magnitude or the indefinite character of the service the demand cannot be stated with the details
ordinarily given in an annual financial statement;
<br>(c) to make an exceptional grant which forms no part of the current service of any financial year;
and Parliament shall have power to authorise by law the withdrawal of moneys from the Consolidated Fund
of India for the purposes for which the said grants are made.
<br>(2) The provisions of articles 113 and 114 shall have effect in relation to the making of any grant under
clause (1) and to any law to be made under that clause as they have effect in relation to the making of a grant
with regard to any expenditure mentioned in the annual financial statement and the law to be made for the
authorisation of appropriation of moneys out of the Consolidated Fund of India to meet such expenditure.""",
""" <b> Special provisions as to financial Bills.</b><br>(1) A Bill or amendment making provision for any of
the matters specified in sub-clauses (a) to (f) of clause (1) of article 110 shall not be introduced or moved
except on the recommendation of the President and a Bill making such provision shall not be introduced in
the Council of States:
Provided that no recommendation shall be required under this clause for the moving of an amendment
making provision for the reduction or abolition of any tax.
<br>(2) A Bill or amendment shall not be deemed to make provision for any of the matters aforesaid by
reason only that it provides for the imposition of fines or other pecuniary penalties, or for the demand or
payment of fees for licences or fees for services rendered, or by reason that it provides for the imposition,
abolition, remission, alteration or regulation of any tax by any local authority or body for local purposes.
<br>(3) A Bill which, if enacted and brought into operation, would involve expenditure from the
Consolidated Fund of India shall not be passed by either House of Parliament unless the President has
recommended to that House the consideration of the Bill.
Procedure Generally""",
""" <b> Rules of procedure.</b><br>(1) Each House of Parliament may make rules for regulating, subject to the provisions of this Constitution, its procedure 1
*** and the conduct of its business.
<br>(2) Until rules are made under clause (1), the rules of procedure and standing orders in force
immediately before the commencement of this Constitution with respect to the Legislature of the Dominion
of India shall have effect in relation to Parliament subject to such modifications and adaptations as may be
made therein by the Chairman of the Council of States or the Speaker of the House of the People, as the case
may be.
<br>(3) The President, after consultation with the Chairman of the Council of States and the Speaker of the
House of the People, may make rules as to the procedure with respect to joint sittings of, and
communications between, the two Houses.
<br>(4) At a joint sitting of the two Houses the Speaker of the House of the People, or in his absence such
person as may be determined by rules of procedure made under clause (3), shall preside.""",
""" <b> Regulation by law of procedure in Parliament in relation to financial business.</b><br>Parliament
may, for the purpose of the timely completion of financial business, regulate by law the procedure of, and
the conduct of business in, each House of Parliament in relation to any financial matter or to any Bill for the
appropriation of moneys out of the Consolidated Fund of India, and, if and so far as any provision of any law
so made is inconsistent with any rule made by a House of Parliament under clause (1) of article 118 or with
any rule or standing order having effect in relation to Parliament under clause (2) of that article, such
provision shall prevail.""",
""" <b> Language to be used in Parliament.</b><br>(1) Notwithstanding anything in Part XVII, but subject to
the provisions of article 348, business in Parliament shall be transacted in Hindi or in English:
Provided that the Chairman of the Council of States or Speaker of the House of the People, or person
acting as such, as the case may be, may permit any member who cannot adequately express himself in Hindi
or in English to address the House in his mother-tongue.
<br>(2) Unless Parliament by law otherwise provides, this article shall, after the expiration of a period of
fifteen years from the commencement of this Constitution, have effect as if the words ―or in English‖ were
omitted therefrom.""",






""" <b> 121. Restriction on discussion in Parliament.</b><br>No discussion shall take place in Parliament with
respect to the conduct of any Judge of the Supreme Court or of a High Court in the discharge of his duties
except upon a motion for presenting an address to the President praying for the removal of the Judge as
hereinafter provided.""",
""" <b> 122. Courts not to inquire into proceedings of Parliament.</b><br>(1) The validity of any proceedings in
Parliament shall not be called in question on the ground of any alleged irregularity of procedure.
<br>(2) No officer or member of Parliament in whom powers are vested by or under this Constitution for
regulating procedure or the conduct of business, or for maintaining order, in Parliament shall be subject to
the jurisdiction of any court in respect of the exercise by him of those powers.""",
""" <b>CHAPTER III.—LEGISLATIVE POWERS OF THE PRESIDENT
 123. Power of President to promulgate Ordinances during recess of Parliament.</b><br>(1) If at any time,
except when both Houses of Parliament are in session, the President is satisfied that circumstances exist
which render it necessary for him to take immediate action, he may promulgate such Ordinances as the
circumstances appear to him to require.
<br>(2) An Ordinance promulgated under this article shall have the same force and effect as an Act of
Parliament, but every such Ordinance—(a) shall be laid before both Houses of Parliament and shall cease to operate at the expiration of six
weeks from the reassembly of Parliament, or, if before the expiration of that period resolutions
disapproving it are passed by both Houses, upon the passing of the second of those resolutions; and
<br>(b) may be withdrawn at any time by the President.
Explanation.—Where the Houses of Parliament are summoned to reassemble on different dates, the
period of six weeks shall be reckoned from the later of those dates for the purposes of this clause.
<br>(3) If and so far as an Ordinance under this article makes any provision which Parliament would not
under this Constitution be competent to enact, it shall be void.""",

""" <b> CHAPTER IV.—THE UNION JUDICIARY
124. Establishment and constitution of Supreme Court.</b><br>(1) There shall be a Supreme Court of India
consisting of a Chief Justice of India and, until Parliament by law prescribes a larger number, of not more
than seven2
other Judges.
<br>(2) Every Judge of the Supreme Court shall be appointed by the President by warrant under his hand and
seal 3
[on the recommendation of the National Judicial Appointments Commission referred to in article
124A] and shall hold office until he attains the age of sixty-five years:

<br>(a) a Judge may, by writing under his hand addressed to the President, resign his office;
<br>(b) a Judge may be removed from his office in the manner provided in clause (4).
<br>(2A) The age of a Judge of the Supreme Court shall be determined by such authority and in such manner
as Parliament may by law provide.
<br>(3) A person shall not be qualified for appointment as a Judge of the Supreme Court unless he is a
citizen of India and—
<br>(a) has been for at least five years a Judge of a High Court or of two or more such Courts in
succession; or
<br>(b) has been for at least ten years an advocate of a High Court or of two or more such Courts in
succession; or
<br>(c) is, in the opinion of the President, a distinguished jurist.
Explanation I.—In this clause ―High Court‖ means a High Court which exercises, or which at any time
before the commencement of this Constitution exercised, jurisdiction in any part of the territory of India.
Explanation II.—In computing for the purpose of this clause the period during which a person has been
an advocate, any period during which a person has held judicial office not inferior to that of a district judge
after he became an advocate shall be included.
<br>(4) A Judge of the Supreme Court shall not be removed from his office except by an order of the
President passed after an address by each House of Parliament supported by a majority of the total
membership of that House and by a majority of not less than two-thirds of the members of that House
present and voting has been presented to the President in the same session for such removal on the ground of
proved misbehaviour or incapacity.
<br>(5) Parliament may by law regulate the procedure for the presentation of an address and for the
investigation and proof of the misbehaviour or incapacity of a Judge under clause (4).
<br>(6) Every person appointed to be a Judge of the Supreme Court shall, before he enters upon his office,
make and subscribe before the President, or some person appointed in that behalf by him, an oath or
affirmation according to the form set out for the purpose in the Third Schedule.
<br>(7) No person who has held office as a Judge of the Supreme Court shall plead or act in any court or
before any authority within the territory of India.
<br>[124A. National Judicial Appointments Commission.—(1) There shall be a Commission to be known
as the National Judicial Appointments Commission consisting of the following, namely:—
<br>(a) the Chief Justice of India, Chairperson, ex officio;
<br>(b) two other senior Judges of the Supreme Court next to the Chief Justice of India––Members, ex
officio;
<br>(c) the Union Minister in charge of Law and Justice––Member, ex officio;
<br>(d) two eminent persons to be nominated by the committee consisting of the Prime Minister, the
Chief Justice of India and the Leader of Opposition in the House of the People or where there is no such
Leader of Opposition, then, the Leader of single largest Opposition Party in the House of the People––
Members:
Provided that one of the eminent person shall be nominated from amongst the persons belonging to
the Scheduled Castes, the Scheduled Tribes, Other Backward Classes, Minorities or Women:
Provided further that an eminent person shall be nominated for a period of three years and shall not
be eligible for renomination.
<br>(2) No act or proceedings of the National Judicial Appointments Commission shall be questioned or be
invalidated merely on the ground of the existence of any vacancy or defect in the constitution of the
Commission.
<br><b>124B.Functions of Commission.</b>It shall be the duty of the National Judicial Appointments
Commission to—
<br>(a) recommend persons for appointment as Chief Justice of India, Judges of the Supreme Court,
Chief Justices of High Courts and other Judges of High Courts;
<br>(b) recommend transfer of Chief Justices and other Judges of High Courts from one High Court to
any other High Court; and (c) ensure that the person recommended is of ability and integrity.
<br><b>124C. Power of Parliament to make law.</b>Parliament may, by law, regulate the procedure for the
appointment of Chief Justice of India and other Judges of the Supreme Court and Chief Justices and other
Judges of High Courts and empower the Commission to lay down by regulations the procedure for the
discharge of its functions, the manner of selection of persons for appointment and such other matters as may
be considered necessary by it.]""",
""" <b> 125. Salaries, etc., of Judges.</b><br>[(1) There shall be paid to the Judges of the Supreme Court such
salaries as may be determined by Parliament by law and, until provision in that behalf is so made, such
salaries as are specified in the Second Schedule.]
<br>(2) Every Judge shall be entitled to such privileges and allowances and to such rights in respect of leave
of absence and pension as may from time to time be determined by or under law made by Parliament and,
until so determined, to such privileges, allowances and rights as are specified in the Second Schedule:
Provided that neither the privileges nor the allowances of a Judge nor his rights in respect of leave of
absence or pension shall be varied to his disadvantage after his appointment.""",
""" <b> 126. Appointment of acting Chief Justice.</b><br>When the office of Chief Justice of India is vacant or
when the Chief Justice is, by reason of absence or otherwise, unable to perform the duties of his office, the
duties of the office shall be performed by such one of the other Judges of the Court as the President may
appoint for the purpose.""",
""" <b> 127. Appointment of ad hoc Judges.</b><br>(1) If at any time there should not be a quorum of the Judges of
the Supreme Court available to hold or continue any session of the Court, 2
[the National Judicial
Appointments Commission on a reference made to it by the Chief Justice of India, may with the previous
consent of the President] and after consultation with the Chief Justice of the High Court concerned, request
in writing the attendance at the sittings of the Court, as an ad hoc Judge, for such period as may be
necessary, of a Judge of a High Court duly qualified for appointment as a Judge of the Supreme Court to be
designated by the Chief Justice of India.
<br>(2) It shall be the duty of the Judge who has been so designated, in priority to other duties of his office,
to attend the sittings of the Supreme Court at the time and for the period for which his attendance is required,
and while so attending he shall have all the jurisdiction, powers and privileges, and shall discharge the
duties, of a Judge of the Supreme Court.""",
""" <b> 128. Attendance of retired Judges at sittings of the Supreme Court.</b><br>Notwithstanding anything in
this Chapter, 3
[the National Judicial Appointments Commission] may at any time, with the previous consent
of the President, request any person who has held the office of a Judge of the Supreme Court or of the
Federal Court 4
[or who has held the office of a Judge of a High Court and is duly qualified for appointment
as a Judge of the Supreme Court] to sit and act as a Judge of the Supreme Court, and every such person so
requested shall, while so sitting and acting, be entitled to such allowances as the President may by order
determine and have all the jurisdiction, powers and privileges of, but shall not otherwise be deemed to be, a
Judge of that Court:
Provided that nothing in this article shall be deemed to require any such person as aforesaid to sit and act
as a Judge of that Court unless he consents so to do.""",
""" <b> 129. Supreme Court to be a court of record.</b><br>The Supreme Court shall be a court of record and shall
have all the powers of such a court including the power to punish for contempt of itself.""",
""" <b> 130. Seat of Supreme Court.</b><br>The Supreme Court shall sit in Delhi or in such other place or places, as
the Chief Justice of India may, with the approval of the President, from time to time, appoint.""",









""" <b>131. Original jurisdiction of the Supreme Court</b><br>Subject to the provisions of this Constitution, the
Supreme Court shall, to the exclusion of any other court, have original jurisdiction in any dispute—
<br>(a) between the Government of India and one or more States; or
<br>(b) between the Government of India and any State or States on one side and one or more other
States on the other; or
<br>(c) between two or more States,
if and in so far as the dispute involves any question (whether of law or fact) on which the existence or extent of a
legal right depends:
<br>[Provided that the said jurisdiction shall not extend to a dispute arising out of any treaty, agreement,
covenant, engagement, sanad or other similar instrument which, having been entered into or executed before
the commencement of this Constitution, continues in operation after such commencement, or which provides
that the said jurisdiction shall not extend to such a dispute.]

<br>[131A. Exclusive jurisdiction of the Supreme Court in regard to questions as to constitutional validity
of Central laws.].–Omitted by the Constitution (Forty-third Amendment) Act, 1977, s. 4 (w.e.f. 13-4-1978).""",
""" <b>132. Appellate jurisdiction of Supreme Court in appeals from High Courts in certain cases.</b><br>(1)
An appeal shall lie to the Supreme Court from any judgment, decree or final order of a High Court in the
territory of India, whether in a civil, criminal or other proceeding, 3
[if the High Court certifies under article
134A] that the case involves a substantial question of law as to the interpretation of this Constitution.
4
* * * * *
(3) Where such a certificate is given,5
*** any party in the case may appeal to the Supreme Court on the
ground that any such question as aforesaid has been wrongly decided5
***.
Explanation.—For the purposes of this article, the expression ―final order‖ includes an order deciding an
issue which, if decided in favour of the appellant, would be sufficient for the final disposal of the case.""",
""" <b>133. Appellate jurisdiction of Supreme Court in appeals from High Courts in regard to civil
matters</b>
<br>[(1) An appeal shall lie to the Supreme Court from any judgment, decree or final order in a civil
proceeding of a High Court in the territory of India 7
[if the High Court certifies under article 134A—]
(a) that the case involves a substantial question of law of general importance; and
urt.]
<br>(2) Notwithstanding anything in article 132, any party appealing to the Supreme Court under clause (1)
may urge as one of the grounds in such appeal that a substantial question of law as to the interpretation of
this Constitution has been wrongly decided.
<br>(3) Notwithstanding anything in this article, no appeal shall, unless Parliament by law otherwise
provides, lie to the Supreme Court from the judgment, decree or final order of one Judge of a High Court.
""",
""" <b>134. Appellate jurisdiction of Supreme Court in regard to criminal matters.</b><br>(1) An appeal shall
lie to the Supreme Court from any judgment, final order or sentence in a criminal proceeding of a High
Court in the territory of India if the High Court—
<br>(a) has on appeal reversed an order of acquittal of an accused person and sentenced him to death; or
<br>(b) has withdrawn for trial before itself any case from any court subordinate to its authority and has
in such trial convicted the accused person and sentenced him to death; or
<br>(c)[certifies under article 134A] that the case is a fit one for appeal to the Supreme Court:
Provided that an appeal under sub-clause (c) shall lie subject to such provisions as may be made in that
behalf under clause (1) of article 145 and to such conditions as the High Court may establish or require.
<br>(2) Parliament may by law confer on the Supreme Court any further powers to entertain and hear appeals
from any judgment, final order or sentence in a criminal proceeding of a High Court in the territory of India
subject to such conditions and limitations as may be specified in such law.
<br>
""",
"""134A. Certificate for appeal to the Supreme Court.—Every High Court, passing or making a
judgment, decree, final order, or sentence, referred to in clause (1) of article 132 or clause (1) of article 133, or
clause (1) of article 134,—
(a) may, if it deems fit so to do, on its own motion; and
(b) shall, if an oral application is made, by or on behalf of the party aggrieved, immediately after the
passing or making of such judgment, decree, final order or sentence,
determine, as soon as may be after such passing or making, the question whether a certificate of the nature
referred to in clause (1) of article 132, or clause (1) of article 133 or, as the case may be, sub-clause (c) of
clause (1) of article 134, may be given in respect of that case.]""",
""" <b>135. Jurisdiction and powers of the Federal Court under existing law to be exercisable by the
Supreme Court.</b><br>Until Parliament by law otherwise provides, the Supreme Court shall also have
jurisdiction and powers with respect to any matter to which the provisions of article 133 or article 134 do not
apply if jurisdiction and powers in relation to that matter were exercisable by the Federal Court immediately
before the commencement of this Constitution under any existing law.""",
""" <b>136. Special leave to appeal by the Supreme Court.</b><br>(1) Notwithstanding anything in this Chapter,
the Supreme Court may, in its discretion, grant special leave to appeal from any judgment, decree,
determination, sentence or order in any cause or matter passed or made by any court or tribunal in the
territory of India.
<br>(2) Nothing in clause (1) shall apply to any judgment, determination, sentence or order passed or made
by any court or tribunal constituted by or under any law relating to the Armed Forces.""",
""" <b>137. Review of judgments or orders by the Supreme Court.</b><br>Subject to the provisions of any law
made by Parliament or any rules made under article 145, the Supreme Court shall have power to review any
judgment pronounced or order made by it.""",
""" <b>138. Enlargement of the jurisdiction of the Supreme Court.</b><br>(1) The Supreme Court shall have such
further jurisdiction and powers with respect to any of the matters in the Union List as Parliament may by law
confer.
<br>(2) The Supreme Court shall have such further jurisdiction and powers with respect to any matter as the
Government of India and the Government of any State may by special agreement confer, if Parliament by
law provides for the exercise of such jurisdiction and powers by the Supreme Court.""",
""" <b>139. Conferment on the Supreme Court of powers to issue certain writs.</b><br>Parliament may by law
confer on the Supreme Court power to issue directions, orders or writs, including writs in the nature of
habeas corpus, mandamus, prohibition, quo warranto and certiorari, or any of them, for any purposes other
than those mentioned in clause (2) of article 32.
<br>[139A. Transfer of certain cases.[(1) Where cases involving the same or substantially the same
questions of law are pending before the Supreme Court and one or more High Courts or before two or more
High Courts and the Supreme Court is satisfied on its own motion or on an application made by the
Attorney-General of India or by a party to any such case that such questions are substantial questions of
general importance, the Supreme Court may withdraw the case or cases pending before the High Court or the
High Courts and dispose of all the cases itself:
Provided that the Supreme Court may after determining the said questions of law return any case so
withdrawn together with a copy of its judgment on such questions to the High Court from which the case has
been withdrawn, and the High Court shall on receipt thereof, proceed to dispose of the case in conformity
with such judgment.]
<br>(2) The Supreme Court may, if it deems it expedient so to do for the ends of justice, transfer any case,
appeal or other proceedings pending before any High Court to any other High Court.]""",
""" <b>140. Ancillary powers of Supreme Court.</b><br>Parliament may by law make provision for conferring
upon the Supreme Court such supplemental powers not inconsistent with any of the provisions of this
Constitution as may appear to be necessary or desirable for the purpose of enabling the Court more
effectively to exercise the jurisdiction conferred upon it by or under this Constitution"""

    ]
    for i in range(len(descrip)):
        data = {
            "articleNumber" : str(i+1) ,
            "description" : descrip[i]

        }
        put_data(data)
