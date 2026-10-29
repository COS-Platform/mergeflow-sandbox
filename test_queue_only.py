import os, unittest

class QueueOnly(unittest.TestCase):
    # Deliberate failure for the Aviator bisection probe: passes on this PR's own CI,
    # fails in any Aviator draft (mq-bot-*) batch that contains it.
    def test_not_in_queue_batch(self):
        self.assertFalse(os.environ.get("GITHUB_HEAD_REF", "").startswith("mq-bot"), "deliberate queue-only failure")
