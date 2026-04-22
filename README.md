# JF Physio — AI Conversation Assistant (POC)

---

## Project Overview for John

**What this is:**
This AI replaces the static "Contact Us" form on your website. Instead of a patient filling in a form and waiting hours (or days) for a reply, they get an instant conversation with a knowledgeable assistant that understands sports and running injuries — the way you do.

**What it does:**
- Talks with patients about their injury in an informed, empathetic way
- Explains which of your services is the right fit for them
- Directs them straight to your Fresha calendar to book — no waiting on email

**Why it matters:**
Every patient who fills in your contact form at 11pm and doesn't get an instant response might book somewhere else by morning. This AI is always on. It captures the lead, has the conversation, and gets them into your calendar while they're still motivated. The contact form was the leak — this is the fix.

---

## For Developers — Setup & Run

### Prerequisites
- Python 3.9 or newer
- An OpenAI API key ([get one here](https://platform.openai.com/api-keys))

### 1. Install dependencies
```bash
cd ~/jfphysio-agent
pip3 install -r requirements.txt
```

### 2. Set up your API key
```bash
cp .env.example .env
```
Open `.env` in any text editor and replace `sk-your-api-key-here` with your real OpenAI key.

### 3. Run the demo
```bash
python3 main.py
```
The bot will greet you first. Type your messages as if you're a patient. Type `bye` or `quit` to end.

---

## For John — How to See the Magic

1. Make sure your developer has set it up (steps above)
2. Open Terminal and type: `python3 ~/jfphysio-agent/main.py`
3. Pretend you're a patient. Try something like:
   - *"My knee's been killing me when I run, especially going downstairs"*
   - *"I've had tight calves for weeks and I think it might be my Achilles"*
   - *"I play rugby and I pulled my hamstring last weekend"*

Watch how the AI talks about the injury intelligently, asks the right questions, and naturally steers toward booking.

---

## Example Conversation

```
💬 JF Physio:  Hey! I'm the JF Physio assistant — here to help with any sports or running 
               injuries you've got going on. What's been bothering you?

You:           My knee hurts when I run, especially going downhill

💬 JF Physio:  Ugh, downhill knee pain is a really common one for runners — and really 
               frustrating when it cuts your sessions short. Can you tell me a bit more 
               about where exactly the pain is? Is it more on the outer side of the knee, 
               around the kneecap, or somewhere else?

You:           Outer side, and it only really kicks in after about 20 minutes

💬 JF Physio:  That pattern — outer knee, starting after a bit of time on your feet — 
               sounds a lot like IT band syndrome. It's one of the most common running 
               injuries John sees. How long has it been going on?

You:           About 3 weeks

💬 JF Physio:  Three weeks is long enough that it's not going to sort itself out without 
               a proper look. The good news is IT band issues respond really well to 
               treatment — John would assess your hip strength and running mechanics and 
               get you a plan. An Initial Assessment is £50 for 45 minutes and he'd start 
               treatment in that same session. The quickest way to lock in a slot is to 
               book directly through his calendar — the contact form can have a delay, 
               but online booking secures your time straight away: 
               https://www.fresha.com/a/jf-physio-darlington-the-offices-faverdale-north-q7f27rno/booking
```

---

## API Cost Estimate

| Metric | Value |
|--------|-------|
| Model | GPT-4o |
| Avg turns per conversation | 10 |
| Estimated cost per conversation | ~$0.05 |
| **Cost per 100 conversations** | **~$5** |
| Cost per 1,000 conversations/month | ~$50/month |

One recovered booking (£50) covers ~1,000 conversations. The ROI pays for itself with a single lead.

---

## Services & Pricing (current as of April 2026)

| Service | Duration | Price |
|---------|----------|-------|
| Initial Assessment & Treatment | 45 mins | £50 |
| Follow-up Treatment | 30 mins | £45 |
| Sports Massage | 45 mins | £45 |
| Acupuncture / Dry Needling | ~45 mins | £45–£50 |

---

## Next Steps (Phase 2)

- **Web widget** — embed as a chat bubble on `jfphysio.co.uk` (using Voiceflow, Botpress, or custom React)
- **WhatsApp** — connect via Twilio or Meta Cloud API for direct WhatsApp conversations
- **Instagram DMs** — via Meta Graph API for the clinic's Instagram channel
- **Lead logging** — save each qualified conversation summary to a Google Sheet or CRM
