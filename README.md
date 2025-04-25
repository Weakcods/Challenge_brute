# Web Application PIN Cracker Challenge

## Challenge Description
This challenge involves creating a Python script to crack a 3-digit PIN protection system on a web server. The script successfully found the correct PIN and gained access to the protected content.

## Challenge Requirements
- Target: Local web server running on port 8888
- PIN Format: 3-digit numeric PIN (000-999)
- Language: Python
- Library Constraint: Only standard socket library allowed

## Success Message
```ascii
           .--.
          |o_o |
          |:_/ |
         //   \\
        (|     |)
       /\\_   _/\\
       \\___)=(___/
       CHALLENGE
       COMPLETED
```

**ACCESS GRANTED - Key accepted. This Drill is done!**

## Solution Process

1. **Server Analysis**
   - Identified server running on localhost:8888
   - Discovered form submission endpoint at `/verify`
   - Found parameter name: `magicNumber`

2. **Challenge Obstacles**
   - Server implemented rate limiting ("whoa, slow down!")
   - Required proper HTTP POST request formatting
   - Needed to handle connection timeouts

3. **Solution Implementation**
   - Created Python script using only socket library
   - Implemented proper POST request formatting
   - Added rate limiting handling with delays
   - Included retry mechanism for failed attempts

4. **Key Features of Solution**
   - Raw socket connection handling
   - Proper HTTP request formatting
   - Rate limit handling with 1-second delays
   - Retry logic for "slow down" responses
   - Response parsing and success detection

## Files Used
- `ctf1_for_x64.exe` - The challenge server
- `pin_brute.py` - The Python solution script
- `server.rar` - Original server package

## Technical Details
The solution script implements:
- Socket-based HTTP communication
- Proper request headers and body formatting
- Rate limiting compliance
- Error handling and retries
- Success detection logic

## Notes
- The server implements rate limiting to prevent rapid-fire attempts
- Proper delays between requests are crucial (1+ second)
- Success is detected by analyzing server response content
- The solution requires patience due to rate limiting

## Request Analysis & Password Guessing Strategy
1. **Initial Response Analysis**
   - Examined server response to understand form structure
   - Found HTML form with:
     ```html
     <form id="magicForm" method="POST" action="/verify">
       <input id="magicNumber" name="magicNumber" type="password" .../>
     ```
   - Identified key parameters:
     - Form endpoint: `/verify`
     - Parameter name: `magicNumber`
     - HTTP method: POST

2. **HTTP Request Structure**
   - Crafted minimal HTTP POST request:
   ```
   POST /verify HTTP/1.1
   Host: 127.0.0.1:8888
   Content-Type: application/x-www-form-urlencoded
   Content-Length: [length]
   Connection: close

   magicNumber=[PIN]
   ```

## Constraints & Solutions

1. **Rate Limiting**
   - **Constraint**: Server responded with "whoa, slow down!" when requests were too frequent
   - **Solution**: 
     - Implemented 1-second delay between attempts
     - Added retry mechanism with exponential backoff
     - Handled rate limit responses gracefully

2. **Connection Management**
   - **Constraint**: Connections could timeout or fail
   - **Solution**:
     - Created new socket for each attempt
     - Implemented proper connection cleanup
     - Added error handling for network issues

3. **Response Processing**
   - **Constraint**: Needed to properly detect success/failure
   - **Solution**:
     - Analyzed HTML responses for success indicators
     - Implemented robust response parsing
     - Added multiple success detection patterns

## Lessons Learned

1. **Network Protocol Understanding**
   - Importance of proper HTTP request formatting
   - Understanding of socket-level network programming
   - Practical experience with HTTP headers and body construction

2. **Security Concepts**
   - Rate limiting as a security measure
   - Brute force attack mechanics
   - PIN-based authentication vulnerabilities

3. **Programming Skills**
   - Raw socket programming in Python
   - Error handling in network applications
   - Response parsing and pattern matching
   - Implementing retry mechanisms

4. **Problem-Solving**
   - Systematic approach to password guessing
   - Adapting to server restrictions
   - Network debugging techniques

## Security Recommendations

1. **Enhanced Rate Limiting**
   - Implement progressive delays for repeated attempts
   - Add IP-based rate limiting
   - Consider temporary IP bans after excessive attempts

2. **Improved Authentication**
   - Increase PIN length (minimum 6 digits)
   - Add account lockout after X failed attempts
   - Implement CAPTCHA or similar challenge-response
   - Add two-factor authentication (2FA)

3. **Request Hardening**
   - Add CSRF protection
   - Implement request signing
   - Use HTTPS/TLS encryption
   - Add request origin validation

4. **Monitoring & Alerts**
   - Log failed authentication attempts
   - Implement real-time attack detection
   - Set up alerts for suspicious activity
   - Add IP reputation checking

5. **Additional Measures**
   - Implement password complexity requirements
   - Add session management
   - Use secure headers (HSTS, CSP, etc.)
   - Regular security audits and penetration testing

## Network Analysis & Discovery
1. **Port Discovery**
   - Used `netstat -ano` command to list all active TCP connections and listening ports
   - Found server listening on port 8888:
   ```
   TCP    0.0.0.0:8888           0.0.0.0:0              LISTENING
   ```
   - The `0.0.0.0` binding indicates the server accepts connections on all network interfaces

2. **Server Address**
   - Server running locally, accessed via:
     - localhost (127.0.0.1)
     - Port 8888
   - Connection verified through initial HTTP request testing

## Challenge Q&A

### Q: How did you find the address and port where the application listens?
A: I used the following methodology to discover the server's location:
1. Used `netstat -ano` command to list all active TCP connections
2. Identified the server listening on port 8888: `TCP 0.0.0.0:8888`
3. The `0.0.0.0` binding indicated it accepts connections on all interfaces
4. Verified the server was accessible via localhost (127.0.0.1)
5. Confirmed connection by sending test HTTP requests

### Q: How did you determine what to send to the server to guess the password?
A: I analyzed the server's behavior through these steps:
1. Made initial connection to view the HTML form
2. Inspected the form structure:
   ```html
   <form id="magicForm" method="POST" action="/verify">
   ```
3. Identified crucial elements:
   - Form method: POST
   - Endpoint: /verify
   - Parameter name: magicNumber
4. Constructed minimal HTTP POST request:
   ```
   POST /verify HTTP/1.1
   Host: 127.0.0.1:8888
   Content-Type: application/x-www-form-urlencoded
   Content-Length: [length]
   Connection: close

   magicNumber=[PIN]
   ```

### Q: What constraints did you encounter and how did you overcome them?
A: The main constraints and solutions were:

1. Rate Limiting:
   - **Problem**: Server responded "whoa, slow down!" for rapid requests
   - **Solution**: 
     * Implemented 1-second delay between attempts
     * Added retry mechanism with exponential backoff
     * Created proper response handling for rate limit messages

2. Connection Management:
   - **Problem**: Connection timeouts and failures
   - **Solution**:
     * Created new socket for each attempt
     * Added proper connection cleanup
     * Implemented comprehensive error handling

3. Response Detection:
   - **Problem**: Needed to accurately detect success/failure
   - **Solution**:
     * Analyzed response patterns
     * Implemented multiple success indicators
     * Added robust response parsing

### Q: What did you learn from this challenge?
A: Key learnings included:

1. Technical Skills:
   - Raw socket programming in Python
   - HTTP protocol structure and formatting
   - Network debugging techniques
   - Rate limit handling strategies

2. Security Concepts:
   - Understanding brute force attack mechanics
   - Importance of rate limiting in security
   - Authentication system vulnerabilities
   - Network security best practices

3. Problem-Solving:
   - Systematic approach to security testing
   - Importance of error handling
   - Value of proper request formatting
   - Network debugging methodology

### Q: What security improvements would you implement to protect against this type of attack?
A: Recommended security improvements:

1. Authentication Enhancements:
   - Increase PIN length (minimum 6 digits)
   - Implement account lockout after X failed attempts
   - Add CAPTCHA or similar challenge-response
   - Enable two-factor authentication (2FA)

2. Rate Limiting Improvements:
   - Progressive delays for repeated attempts
   - IP-based rate limiting
   - Temporary IP bans for excessive attempts
   - Distributed rate limiting across multiple servers

3. Infrastructure Security:
   - Implement HTTPS/TLS encryption
   - Add request origin validation
   - Enable secure headers (HSTS, CSP)
   - Implement IP reputation checking

4. Monitoring and Response:
   - Real-time attack detection
   - Automated alerting system
   - Comprehensive security logging
   - Incident response procedures

5. Additional Measures:
   - Session management
   - CSRF protection
   - Request signing
   - Regular security audits