import unittest
from .solution import spin_solve


class SolutionTest(unittest.TestCase):
    def test_spin_solve(self):
        self.assertEqual(
            "emocleW.",
            spin_solve("Welcome.")
        )

        self.assertEqual(
            "IF 0 man does not keep pace with his snoinapmoc, spahrep IT IS esuaceb HE hears 0 tnereffid remmurd.",
            spin_solve("If a man does not keep pace with his companions, perhaps it is because he hears a different drummer.")
        )

        self.assertEqual(
            "AS reiniarG drove along IN the wagon behind 0 WIDE, SLOW, deroloc-dnas MARE, sretsulc OF orange seilfrettub dedolpxe off the purple hsikcalb piles OF bear sign and winked and winked and derettulf yllacigam like leaves tuohtiw trees.",
            spin_solve(
                "As Grainier drove along in the wagon behind a wide, slow, sand-colored mare, clusters of orange butterflies exploded off the purple blackish piles of bear sign and winked and winked and fluttered magically like leaves without trees.")
        )

        self.assertEqual(
            "You should check the egaelim ON your car since you've been gnivird IT SO MUCH, and esuaceb it's gnitrats TO make weird noises.",
            spin_solve("You should check the mileage on your car since you've been driving it so much, and because it's starting to make weird noises.")
        )

        self.assertEqual(
            "reverehW you GO, you can always find beauty.",
            spin_solve("Wherever you go, you can always find beauty.")
        )

        self.assertEqual(
            "Action IS INDEED, gnimmmmmmmmoc.",
            spin_solve("Action is indeed, commmmmmmming.")
        )

        self.assertEqual(
            "MOTHER, PLEASE, HELP, ME.",
            spin_solve("Mother, please, help, me.")
        )

        self.assertEqual(
            "JOJOJO, JOJO, atat man kata.",
            spin_solve("Jojojo, jojo, tata man kata.")
        )



if __name__ == '__main__':
    unittest.main()
