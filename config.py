"""
BUSINESS CONFIGURATION — edit this file to adapt the assistant to any business.
Everything the AI knows about the business lives here.
"""

BUSINESS_CONFIG = {
    # ── Core Identity ──────────────────────────────────────────────────────────
    "name": "Apex Wellness Studio",
    "tagline": "Health, Recovery & Performance",
    "location": "12 High Street, Darlington DL1 1AA",
    "phone": "01325 000000",
    "email": "hello@apexwellness.co.uk",
    "booking_url": "https://booking.example.com",
    "page_icon": "💪",

    # ── Services ───────────────────────────────────────────────────────────────
    # Add, remove, or edit services freely
    "services": [
        {
            "name": "Initial Consultation",
            "price": "£60",
            "duration": "60 mins",
            "description": "Full assessment of your goals, health history, and a personalised plan.",
            "primary": True,   # Mark one as the primary recommendation for new customers
        },
        {
            "name": "Sports Recovery Session",
            "price": "£45",
            "duration": "45 mins",
            "description": "Deep tissue work, mobility, and recovery protocols for active people.",
            "primary": False,
        },
        {
            "name": "Performance Programme",
            "price": "£120/month",
            "duration": "Ongoing",
            "description": "Monthly coaching and treatment package for serious athletes.",
            "primary": False,
        },
    ],

    # ── Expertise Areas ────────────────────────────────────────────────────────
    # What does this business specialise in? Used to shape the AI's knowledge base.
    "expertise": [
        "Sports recovery and injury prevention",
        "Strength and conditioning for recreational athletes",
        "Mobility and flexibility training",
        "Nutrition guidance for active lifestyles",
        "Return-to-sport programmes after injury",
    ],

    # ── Assistant Persona ──────────────────────────────────────────────────────
    # How should the AI come across? Adjust tone to match the brand.
    "persona": (
        "You are warm, knowledgeable, and direct — like a trusted coach who happens to know "
        "the science. You speak plainly, avoid jargon unless the customer uses it first, "
        "and genuinely care about helping people reach their goals. "
        "CRITICAL: Never exceed 3 sentences per response. Be concise — one clear point per "
        "message. If you have more to say, ask a follow-up question instead."
    ),

    # ── Booking Urgency Message ────────────────────────────────────────────────
    # Why should they book online rather than email/call?
    "booking_urgency": (
        "Online booking is the fastest way to secure a slot — the inbox can have a 24–48 hour "
        "delay, but booking directly locks in your time instantly."
    ),

    # ── Out-of-Scope Redirect ──────────────────────────────────────────────────
    "out_of_scope_response": (
        "That's a bit outside what I can help with here — happy to answer anything about "
        "our services, your health goals, or getting booked in though!"
    ),

    # ── Red Flag Escalation ────────────────────────────────────────────────────
    # Describe any situations where the AI should escalate rather than book
    "red_flags": (
        "If the customer describes severe acute symptoms (chest pain, inability to breathe, "
        "sudden severe swelling, loss of consciousness), advise them to call 999 or go to A&E "
        "immediately. Do not minimise this."
    ),
}
