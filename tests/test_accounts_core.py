import unittest
from accounts_core.engine import ERPNextAccountsCoreEngine, GLEntry

class TestAccountsCore(unittest.TestCase):
    def test_double_entry_validation(self):
        engine = ERPNextAccountsCoreEngine()
        entries = [
            GLEntry("2026-04-01", "Bank Account - HDFC", 10000.0, 0.0, "Journal Entry", "JV-001"),
            GLEntry("2026-04-01", "Sales Revenue", 0.0, 10000.0, "Journal Entry", "JV-001")
        ]
        self.assertTrue(engine.validate_double_entry_balance(entries))

    def test_trial_balance_computation(self):
        engine = ERPNextAccountsCoreEngine()
        entries = [
            GLEntry("2026-04-01", "Debtors", 5000.0, 0.0, "Sales Invoice", "SINV-01"),
            GLEntry("2026-04-01", "Sales", 0.0, 5000.0, "Sales Invoice", "SINV-01")
        ]
        tb = engine.compute_trial_balance(entries)
        self.assertTrue(tb.is_balanced)
        self.assertEqual(tb.total_debit, 5000.0)
        self.assertEqual(tb.total_credit, 5000.0)

if __name__ == "__main__":
    unittest.main()
